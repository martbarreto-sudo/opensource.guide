#!/usr/bin/env python3
"""
check_artifacts_clean.py — Fail CI if build/cache/CI residue leaks secrets.

Rationale
---------
Secrets rarely leak from source; they leak from *derived* material — build
output, caches, logs, throwaway databases left behind by the test run. This
gate scans the usual residue directories and flags anything that looks like a
credential, so a green pipeline can't quietly publish a token.

What it scans (defaults, override with --dir / --glob):
  build/  dist/  .pytest_cache/  __pycache__/  .cache/  tmp/  temp/  node_modules/.cache/
  plus files matching  *.log  *.sqlite*  *.tmp  *.env  *.pem  *.key

Detection: a curated set of high-signal regexes (AWS, GCP, private keys,
GitHub/Slack tokens, JWTs, generic assignments) plus a light entropy check on
long opaque strings. Binary files are skipped by content sniff.

Exit codes: 0 = clean, 1 = potential secret(s) found, 2 = usage error.

Usage
-----
  python scripts/check_artifacts_clean.py
  python scripts/check_artifacts_clean.py --dir build --dir dist --strict
  python scripts/check_artifacts_clean.py --allow allowlist.txt
"""
from __future__ import annotations

import argparse
import math
import os
import re
import sys
from pathlib import Path
from typing import Iterable, List, Tuple

DEFAULT_DIRS = [
    "build", "dist", ".pytest_cache", "__pycache__", ".cache",
    "tmp", "temp", "node_modules/.cache",
]
DEFAULT_GLOBS = ["*.log", "*.sqlite", "*.sqlite3", "*.db", "*.tmp", "*.env", "*.pem", "*.key"]

# name -> compiled pattern. Kept deliberately high-signal to limit false positives.
PATTERNS: List[Tuple[str, "re.Pattern[str]"]] = [
    ("AWS Access Key ID", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("AWS Secret Access Key", re.compile(r"(?i)aws.{0,20}?(secret|access).{0,20}?['\"][0-9a-zA-Z/+]{40}['\"]")),
    ("Private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[0-9A-Za-z]{36,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("Stripe live key", re.compile(r"\bsk_live_[0-9A-Za-z]{16,}\b")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\b")),
    ("Generic secret assignment", re.compile(
        r"(?i)(password|passwd|secret|token|api[_-]?key|access[_-]?key)"
        r"\s*[:=]\s*['\"][^'\"\s]{8,}['\"]")),
]

# Substrings that neutralize an otherwise-matching line (obvious placeholders).
PLACEHOLDERS = ("example", "dummy", "placeholder", "changeme", "your_", "xxxxxxxx", "redacted", "<", "test-token")


def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    counts = {c: s.count(c) for c in set(s)}
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())


def looks_binary(path: Path) -> bool:
    try:
        chunk = path.open("rb").read(2048)
    except OSError:
        return True
    if b"\x00" in chunk:
        return True
    # >30% non-text bytes → treat as binary
    text = bytes(range(32, 127)) + b"\n\r\t\f\b"
    nontext = sum(b not in text for b in chunk)
    return bool(chunk) and nontext / len(chunk) > 0.30


def iter_targets(root: Path, dirs: Iterable[str], globs: Iterable[str]) -> Iterable[Path]:
    seen: set[Path] = set()
    for d in dirs:
        base = root / d
        if base.is_dir():
            for p in base.rglob("*"):
                if p.is_file() and p not in seen:
                    seen.add(p)
                    yield p
    for g in globs:
        for p in root.rglob(g):
            if p.is_file() and p not in seen:
                seen.add(p)
                yield p


def scan_file(path: Path, entropy_threshold: float) -> List[Tuple[int, str, str]]:
    findings: List[Tuple[int, str, str]] = []
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            for lineno, line in enumerate(fh, 1):
                if len(line) > 4000:  # avoid pathological minified lines
                    line = line[:4000]
                low = line.lower()
                for name, pat in PATTERNS:
                    if pat.search(line) and not any(ph in low for ph in PLACEHOLDERS):
                        findings.append((lineno, name, line.strip()[:160]))
                # entropy heuristic on long opaque tokens
                for tok in re.findall(r"[A-Za-z0-9+/=_\-]{24,}", line):
                    if shannon_entropy(tok) >= entropy_threshold and not any(ph in low for ph in PLACEHOLDERS):
                        findings.append((lineno, "High-entropy string", tok[:64]))
                        break
    except OSError as e:
        print(f"::warning::could not read {path}: {e}", file=sys.stderr)
    return findings


def load_allowlist(path: str | None) -> set[str]:
    if not path:
        return set()
    try:
        return {ln.strip() for ln in Path(path).read_text().splitlines()
                if ln.strip() and not ln.startswith("#")}
    except OSError:
        return set()


def main() -> int:
    ap = argparse.ArgumentParser(description="Fail if build/cache/CI residue contains secrets.")
    ap.add_argument("--root", default=".", help="Repository root to scan (default: .).")
    ap.add_argument("--dir", action="append", default=None, help="Extra directory to scan (repeatable).")
    ap.add_argument("--glob", action="append", default=None, help="Extra filename glob (repeatable).")
    ap.add_argument("--allow", help="Path to allowlist file (one substring per line to ignore).")
    ap.add_argument("--entropy", type=float, default=4.3, help="Shannon-entropy threshold (default: 4.3).")
    ap.add_argument("--strict", action="store_true", help="Also treat high-entropy-only hits as failures.")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"::error::root '{root}' is not a directory", file=sys.stderr)
        return 2

    dirs = DEFAULT_DIRS + (args.dir or [])
    globs = DEFAULT_GLOBS + (args.glob or [])
    allow = load_allowlist(args.allow)

    total = 0
    scanned = 0
    for path in iter_targets(root, dirs, globs):
        if looks_binary(path):
            continue
        scanned += 1
        rel = path.relative_to(root)
        for lineno, kind, snippet in scan_file(path, args.entropy):
            if any(a in snippet or a in str(rel) for a in allow):
                continue
            if kind == "High-entropy string" and not args.strict:
                # In non-strict mode, entropy alone is a warning, not a failure.
                print(f"::warning file={rel},line={lineno}::possible secret ({kind}): {snippet}")
                continue
            total += 1
            print(f"::error file={rel},line={lineno}::potential secret ({kind}): {snippet}",
                  file=sys.stderr)

    if total:
        print(f"\n✗ check-artifacts-clean: {total} potential secret(s) across {scanned} scanned file(s).",
              file=sys.stderr)
        print("  Remove the residue (add to .gitignore / clean the build step) or, if a true "
              "false positive, add a substring to the --allow file.", file=sys.stderr)
        return 1

    print(f"✓ check-artifacts-clean: no secrets found in {scanned} scanned artifact file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
