#!/usr/bin/env bash
#
# changelog-add.sh — append an entry to the [Unreleased] section of CHANGELOG.md.
#
# Usage:
#   bash scripts/changelog-add.sh "feat(regulatory-guard): add CCPA opt-out check"
#   bash scripts/changelog-add.sh --type fix --scope convex "race in cron scheduler"
#
# Designed to be safe for AI agents to call: idempotent (won't duplicate identical
# lines), creates [Unreleased] section if missing, never rewrites existing entries.
#
# Exit codes: 0 OK, 1 misuse, 2 IO error.

set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHANGELOG="$ROOT/CHANGELOG.md"

usage() {
  cat <<'EOF'
Usage:
  scripts/changelog-add.sh "<conventional-commit-style entry>"
  scripts/changelog-add.sh --type <feat|fix|chore|docs|refactor|perf|test> [--scope <name>] "<message>"

Examples:
  scripts/changelog-add.sh "feat(regulatory-guard): add EAA accessibility audit"
  scripts/changelog-add.sh --type fix --scope ci "release script handles empty changelog"
EOF
}

if [[ $# -eq 0 ]]; then
  usage
  exit 1
fi

type=""
scope=""
msg=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help) usage; exit 0 ;;
    --type)    type="$2"; shift 2 ;;
    --scope)   scope="$2"; shift 2 ;;
    --)        shift; msg="$*"; break ;;
    *)         msg="$1"; shift ;;
  esac
done

if [[ -z "$msg" ]]; then
  echo "error: missing message"
  usage
  exit 1
fi

# Build entry.
if [[ -n "$type" ]]; then
  if [[ -n "$scope" ]]; then
    entry="- ${type}(${scope}): ${msg}"
  else
    entry="- ${type}: ${msg}"
  fi
else
  # Free-form — assume user passed a conventional-commit-style line.
  entry="- ${msg}"
fi

if [[ ! -f "$CHANGELOG" ]]; then
  echo "error: $CHANGELOG not found" >&2
  exit 2
fi

# Idempotency: bail if exact line already in file.
# Use `--` so leading `-` in $entry isn't parsed as a grep option.
if grep -Fxq -- "$entry" "$CHANGELOG"; then
  echo "skip  entry already present: $entry"
  exit 0
fi

# Insert under [Unreleased]; create the section if it doesn't exist.
tmp="$(mktemp)"
if grep -q '^## \[Unreleased\]' "$CHANGELOG"; then
  awk -v new="$entry" '
    BEGIN { inserted=0 }
    /^## \[Unreleased\]/ {
      print
      # consume blank line if present
      getline next_line
      if (next_line ~ /^[[:space:]]*$/) {
        print next_line
      } else {
        print ""
        print next_line
      }
      print new
      inserted=1
      next
    }
    { print }
  ' "$CHANGELOG" > "$tmp"
else
  awk -v new="$entry" '
    BEGIN { inserted=0 }
    /^# Changelog/ && inserted==0 {
      print
      getline next_line
      print next_line
      print ""
      print "## [Unreleased]"
      print ""
      print new
      inserted=1
      next
    }
    { print }
  ' "$CHANGELOG" > "$tmp"
fi

mv "$tmp" "$CHANGELOG"
echo "added $entry"
