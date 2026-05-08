#!/usr/bin/env bash
#
# release.sh — bump version, promote [Unreleased] → [x.y.z], tag, push.
#
# Designed for AI agents and humans alike. Non-interactive — pass --bump explicitly.
#
# Usage:
#   bash scripts/release.sh --bump patch    # 0.1.0 -> 0.1.1
#   bash scripts/release.sh --bump minor    # 0.1.0 -> 0.2.0
#   bash scripts/release.sh --bump major    # 0.1.0 -> 1.0.0
#   bash scripts/release.sh --bump patch --dry-run
#
# Steps:
#   1. Verify clean working tree on main
#   2. Verify [Unreleased] has at least one entry
#   3. Compute next version from latest git tag
#   4. Rename [Unreleased] -> [x.y.z] - YYYY-MM-DD, add new empty [Unreleased]
#   5. Commit, tag, push (unless --dry-run)
#
# CI's publish workflow picks up the tag and creates the GitHub Release.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

bump=""
dry_run=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --bump)    bump="$2"; shift 2 ;;
    --dry-run) dry_run=1; shift ;;
    -h|--help)
      sed -n '2,20p' "$0"
      exit 0 ;;
    *)
      echo "error: unknown arg: $1" >&2
      exit 1 ;;
  esac
done

if [[ ! "$bump" =~ ^(patch|minor|major)$ ]]; then
  echo "error: --bump must be one of patch|minor|major" >&2
  exit 1
fi

# 1. clean working tree
if [[ -n "$(git status --porcelain)" ]]; then
  echo "error: working tree not clean — commit or stash first" >&2
  exit 1
fi

branch="$(git rev-parse --abbrev-ref HEAD)"
if [[ "$branch" != "main" ]]; then
  echo "error: must be on main (currently on $branch)" >&2
  exit 1
fi

# 2. unreleased has entries
if ! awk '/^## \[Unreleased\]/{flag=1; next} /^## \[/{flag=0} flag' CHANGELOG.md | grep -qE '^- '; then
  echo "error: [Unreleased] section is empty — add entries via scripts/changelog-add.sh" >&2
  exit 1
fi

# 3. compute next version
latest_tag="$(git tag --list 'v*' --sort=-version:refname | grep -v canary | head -1 || true)"
if [[ -z "$latest_tag" ]]; then
  current="0.0.0"
else
  current="${latest_tag#v}"
fi

IFS='.' read -r major minor patch <<< "$current"
case "$bump" in
  major) major=$((major + 1)); minor=0; patch=0 ;;
  minor) minor=$((minor + 1)); patch=0 ;;
  patch) patch=$((patch + 1)) ;;
esac
next="${major}.${minor}.${patch}"
next_tag="v${next}"
today="$(date -u +%Y-%m-%d)"

echo "release: $latest_tag -> $next_tag (date: $today)"

# 4. rewrite CHANGELOG: [Unreleased] -> [x.y.z] - date, prepend new empty [Unreleased]
tmp="$(mktemp)"
awk -v ver="$next" -v date="$today" '
  /^## \[Unreleased\]/ && replaced==0 {
    print "## [Unreleased]"
    print ""
    print "## [" ver "] - " date
    replaced=1
    next
  }
  { print }
' CHANGELOG.md > "$tmp"

if [[ "$dry_run" -eq 1 ]]; then
  echo "--- CHANGELOG.md (preview) ---"
  head -40 "$tmp"
  echo "--- (dry-run, not committing) ---"
  rm "$tmp"
  exit 0
fi

mv "$tmp" CHANGELOG.md

# 5. commit + tag + push
git add CHANGELOG.md
git commit -m "chore(release): ${next_tag}"
git tag -a "$next_tag" -m "$next_tag"
git push origin main
git push origin "$next_tag"

echo "released $next_tag"
echo "GitHub release will be created automatically by .github/workflows/publish.yml"
