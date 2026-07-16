# `.claude/` — SessionStart provisioning

Technical architecture guide for the automation that prepares the
`opensource.guide` Jekyll site to build, test and serve inside
**Claude Code on the web** sessions.

> **TL;DR** — On every session start, a hook detects the remote (web)
> environment, persists a UTF-8 locale and the `PAGES_REPO_NWO` variable,
> then runs `script/bootstrap` to install Ruby + Node dependencies. On a
> local machine it is a no-op. Net result: `script/build`, `script/test`
> and `script/server` work out of the box in a fresh web container.

---

## 1. Architecture

```
[Claude Code Web Init]
        │
        ▼
.claude/settings.json ───────►  registers a SessionStart command hook
        │
        ▼
.claude/hooks/session-start.sh
        │
        ├─ gate:   CLAUDE_CODE_REMOTE != "true"  ──►  exit 0   (local: no-op)
        │
        ├─ env:    LANG / LC_ALL = C.utf8
        │          PAGES_REPO_NWO = github/opensource.guide      ──►  $CLAUDE_ENV_FILE
        │
        └─ deps:   script/bootstrap  ──►  bundle install + npm install
                       │
                       └─ stdout+stderr ──► .claude/hooks/bootstrap.log  (git-ignored)
        │
        ▼
[Operational environment]  —  build / test / serve ready
```

The pipeline is **synchronous**: the session does not become interactive
until the hook returns. That is deliberate — it guarantees dependencies are
present before any build/test command can run, at the cost of a one-time
boot delay.

---

## 2. Files

| File | Role |
| --- | --- |
| `.claude/settings.json` | Registers the `SessionStart` command hook. |
| `.claude/hooks/session-start.sh` | The provisioning script (guard → env → bootstrap). |
| `.claude/.gitignore` | Ignores the generated `hooks/bootstrap.log`. |

### `.claude/settings.json`

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/session-start.sh"
          }
        ]
      }
    ]
  }
}
```

### `.claude/hooks/session-start.sh`

See the file for the full source. Its shape is: `set -euo pipefail` →
environment gate → append env vars to `$CLAUDE_ENV_FILE` → run
`script/bootstrap` with output redirected to `bootstrap.log`.

---

## 3. Execution flow

| Step | What happens | Why |
| --- | --- | --- |
| **0 — Gate** | If `CLAUDE_CODE_REMOTE != "true"`, `exit 0`. | Local and CI setups are provably untouched; the hook only acts in the cloud. |
| **1 — Env** | Append `LANG`, `LC_ALL` (`C.utf8`) and `PAGES_REPO_NWO` to `$CLAUDE_ENV_FILE`. | Persisting (vs. plain `export`) makes the values survive into every later tool call in the session, not only this script. |
| **2 — Deps** | Run `script/bootstrap`, logging to `.claude/hooks/bootstrap.log`. On a non-zero exit the hook prints the log tail and aborts. | Reuses the repo's own bootstrap — the same path humans use — instead of reinventing install. Failing loudly prevents a "false green" session that would break on the first build. |
| **3 — Ready** | Print a one-line confirmation. | The session can now build, test and serve. |

---

## 4. Why these environment variables

| Variable | Reason |
| --- | --- |
| `LANG` / `LC_ALL = C.utf8` | Fresh web containers start with an empty locale. The SCSS converter dies on non-ASCII bytes during the Jekyll build unless a UTF-8 locale is set. |
| `PAGES_REPO_NWO = github/opensource.guide` | Required by the `jekyll-github-metadata` plugin to resolve `site.github.*`; the build refuses to run without it. |

---

## 5. Verification

Run from the repo root with the toolchain installed:

```bash
script/build   # jekyll build
script/test    # build + rake + html-proofer + prose check
script/server  # live preview on :4000
```

Latest verified local run of the unit suite (`bundle exec rake`):

```
338 runs, 2691 assertions, 0 failures, 0 errors, 0 skips
```

The test-config Jekyll build completes cleanly (~15s). No external
credentials or network services are required for the unit suite.

`script/bootstrap` is Bundler-version-agnostic: it configures the install
path with `bundle config set --local path vendor/gems` and generates
binstubs with `bundle binstubs --all`, instead of the removed
`--path` / `--binstubs` install flags. A failed gem install aborts the
script (and the hook), so a session can never start with missing
dependencies.

---

## 6. Design principles

- **Guard first.** The environment check is the very first statement — the
  hook is a strict no-op outside the web.
- **Persist, don't export.** State goes to `$CLAUDE_ENV_FILE` so it outlives
  the script.
- **Reuse existing scripts.** The hook drives `script/bootstrap`, not a
  parallel install path.
- **Quiet logs, clean tree.** Install noise goes to a git-ignored
  `bootstrap.log`; the working tree and session context stay clean.
