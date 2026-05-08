#!/usr/bin/env bash
# Install project-managed git hooks. Run once after clone.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
git config core.hooksPath .githooks
chmod +x .githooks/* scripts/*.sh
echo "hooks installed: core.hooksPath=.githooks"
