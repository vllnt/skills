#!/usr/bin/env bash
#
# release-prep.sh — open a release PR that promotes [Unreleased] -> [x.y.z].
#
# This is the ONLY way to land a release commit on main. Branch protection
# requires a PR for any commit on main — including the version bump.
#
# Usage:
#   bash scripts/release-prep.sh --bump patch    # 0.1.0 -> 0.1.1
#   bash scripts/release-prep.sh --bump minor
#   bash scripts/release-prep.sh --bump major
#   bash scripts/release-prep.sh --bump patch --dry-run
#
# Steps:
#   1. Verify clean working tree on main, [Unreleased] non-empty
#   2. Compute next version from latest git tag
#   3. Create branch release/vX.Y.Z, promote [Unreleased] -> [X.Y.Z] - YYYY-MM-DD
#   4. Push branch + open PR via gh
#
# After the PR squash-merges, dispatch "Publish" workflow to tag main HEAD.

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
      sed -n '2,20p' "$0"; exit 0 ;;
    *) echo "error: unknown arg: $1" >&2; exit 1 ;;
  esac
done

if [[ ! "$bump" =~ ^(patch|minor|major)$ ]]; then
  echo "error: --bump must be one of patch|minor|major" >&2
  exit 1
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "error: working tree not clean — commit or stash first" >&2
  exit 1
fi

git fetch origin
git checkout main
git pull --ff-only origin main

if ! awk '/^## \[Unreleased\]/{flag=1; next} /^## \[/{flag=0} flag' CHANGELOG.md | grep -qE '^- '; then
  echo "error: [Unreleased] section is empty — add entries via scripts/changelog-add.sh" >&2
  exit 1
fi

latest_tag="$(git tag --list 'v*' --sort=-version:refname | grep -v canary | head -1 || true)"
current="${latest_tag#v}"
[[ -z "$current" ]] && current="0.0.0"

IFS='.' read -r major minor patch <<< "$current"
case "$bump" in
  major) major=$((major + 1)); minor=0; patch=0 ;;
  minor) minor=$((minor + 1)); patch=0 ;;
  patch) patch=$((patch + 1)) ;;
esac
next="${major}.${minor}.${patch}"
next_tag="v${next}"
today="$(date -u +%Y-%m-%d)"
branch="release/${next_tag}"

echo "release-prep: ${latest_tag:-(none)} -> ${next_tag} (date: $today)"

if git rev-parse --verify "$next_tag" >/dev/null 2>&1; then
  echo "error: tag $next_tag already exists locally" >&2
  exit 1
fi

if git ls-remote --exit-code origin "refs/tags/$next_tag" >/dev/null 2>&1; then
  echo "error: tag $next_tag already exists on remote" >&2
  exit 1
fi

# Promote [Unreleased] -> [next] - today
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
  head -30 "$tmp"
  echo "--- (dry-run, branch + PR not created) ---"
  rm "$tmp"
  exit 0
fi

mv "$tmp" CHANGELOG.md

git checkout -b "$branch"
git add CHANGELOG.md
git commit -m "chore(release): ${next_tag}"
git push -u origin "$branch"

# Open PR
notes=$(awk "/^## \\[${next}\\]/{found=1; next} /^## \\[/{if(found) exit} found{print}" CHANGELOG.md)

gh pr create \
  --base main --head "$branch" \
  --title "chore(release): ${next_tag}" \
  --body "$(cat <<EOF
Promotes \`[Unreleased]\` to \`[${next}] - ${today}\`.

After this merges (squash), dispatch the **Publish** workflow on \`main\` to create tag \`${next_tag}\` and publish the GitHub Release.

## Changelog

${notes}
EOF
)"

echo ""
echo "release-prep done."
echo "next: review + squash-merge the PR, then Actions -> Publish -> Run workflow"
