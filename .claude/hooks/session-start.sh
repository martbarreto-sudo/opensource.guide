#!/bin/bash
# SessionStart hook: prepare the opensource.guide Jekyll site so the build,
# tests and link/prose checks work in Claude Code on the web sessions.
set -euo pipefail

# Only run in the remote (web) environment; local setups are left untouched.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# Persist the environment the build needs:
#  - A UTF-8 locale, otherwise the SCSS converter dies on non-ASCII bytes
#    (LANG is empty in fresh web containers).
#  - PAGES_REPO_NWO, required by the jekyll-github-metadata plugin.
{
  echo 'export LANG=C.utf8'
  echo 'export LC_ALL=C.utf8'
  echo 'export PAGES_REPO_NWO=github/opensource.guide'
} >> "$CLAUDE_ENV_FILE"

# Install Ruby gems (with binstubs in bin/) and node dependencies.
# Output is logged to keep the session context clean; bootstrap is idempotent.
LANG=C.utf8 LC_ALL=C.utf8 script/bootstrap > .claude/hooks/bootstrap.log 2>&1

echo "session-start hook: dependencies installed, build env configured"
