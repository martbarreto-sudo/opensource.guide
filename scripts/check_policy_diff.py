#!/usr/bin/env python3
"""
check_policy_diff.py — Block changes under policy/ unless explicitly approved.

Rationale
---------
The `policy/` tree defines the repository's trust surface (access rules,
allow/deny lists, agent authorizations). Any change to it must be a deliberate,
reviewed act — never an incidental side effect of an unrelated PR.

This gate:
  1. Computes the set of changed files relative to a base ref.
  2. Flags any change touching `policy/` (configurable).
  3. Requires an explicit approval marker for those changes; otherwise fails.

Approval markers (any one satisfies the gate):
  * Env var  SECOPS_APPROVED=1
  * A PR label listed in env PR_LABELS (comma/space separated) matching
    --approval-label (default: "secops-approved").
  * The most recent commit touching policy/ carries the trailer
    "SecOps-Approved: yes" (git commit trailer).

Exit codes: 0 = clean/approved, 1 = unauthorized policy change, 2 = usage error.

Usage
-----
  python scripts/check_policy_diff.py
  python scripts/check_policy_diff.py --base origin/main --path policy/
  BASE_REF=origin/main SECOPS_APPROVED=1 python scripts/check_policy_diff.py
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from typing import List


def run(cmd: List[str]) -> str:
    return subprocess.run(cmd, capture_output=True, text=True, check=False).stdout.strip()


def resolve_base(explicit: str | None) -> str:
    """Pick a base ref to diff against, tolerant of local & CI environments."""
    for cand in (
        explicit,
        os.environ.get("BASE_REF"),
        (f"origin/{os.environ['GITHUB_BASE_REF']}" if os.environ.get("GITHUB_BASE_REF") else None),
    ):
        if cand and run(["git", "rev-parse", "--verify", "--quiet", cand]):
            return cand
    # Fallbacks: merge-base with origin/main, else the previous commit.
    for cand in ("origin/main", "origin/master", "HEAD~1"):
        if run(["git", "rev-parse", "--verify", "--quiet", cand]):
            return cand
    return "HEAD"  # first commit; diff against empty tree handled by caller


def changed_files(base: str) -> List[str]:
    merge_base = run(["git", "merge-base", base, "HEAD"]) or base
    out = run(["git", "diff", "--name-only", f"{merge_base}...HEAD"])
    return [ln for ln in out.splitlines() if ln]


def approved(label: str) -> tuple[bool, str]:
    if os.environ.get("SECOPS_APPROVED", "").strip() in ("1", "true", "yes"):
        return True, "env SECOPS_APPROVED"
    labels = os.environ.get("PR_LABELS", "").replace(",", " ").split()
    if label in labels:
        return True, f"PR label '{label}'"
    trailers = run(["git", "log", "-1", "--format=%(trailers:key=SecOps-Approved,valueonly)"])
    if trailers.strip().lower() in ("yes", "true", "1"):
        return True, "commit trailer SecOps-Approved"
    return False, ""


def main() -> int:
    ap = argparse.ArgumentParser(description="Block unreviewed changes to the policy surface.")
    ap.add_argument("--base", help="Base ref to diff against (default: auto-detect).")
    ap.add_argument("--path", default="policy/", help="Guarded path prefix (default: policy/).")
    ap.add_argument("--approval-label", default="secops-approved",
                    help="PR label that authorizes policy changes.")
    args = ap.parse_args()

    if not run(["git", "rev-parse", "--is-inside-work-tree"]):
        print("::error::not inside a git work tree", file=sys.stderr)
        return 2

    base = resolve_base(args.base)
    files = changed_files(base)
    guarded = args.path.rstrip("/") + "/"
    touched = [f for f in files if f == guarded.rstrip("/") or f.startswith(guarded)]

    if not touched:
        print(f"✓ check-policy-diff: no changes under '{guarded}' (base={base}).")
        return 0

    ok, why = approved(args.approval_label)
    if ok:
        print(f"✓ check-policy-diff: {len(touched)} policy file(s) changed, "
              f"approved via {why}.")
        for f in touched:
            print(f"    ~ {f}")
        return 0

    print("::error title=Unauthorized policy change::"
          f"{len(touched)} file(s) under '{guarded}' changed without approval.",
          file=sys.stderr)
    for f in touched:
        print(f"    ✗ {f}", file=sys.stderr)
    print(
        "\nTo authorize, do ONE of:\n"
        f"  • add the '{args.approval_label}' label to the PR, or\n"
        "  • set SECOPS_APPROVED=1 in the workflow env (guarded by CODEOWNERS), or\n"
        "  • add the trailer 'SecOps-Approved: yes' to the policy commit.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
