#!/usr/bin/env bash
# Exercise the hook against staged content in an isolated repository.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
REPO="$TMP/fixture"

mkdir -p "$REPO/.githooks" "$REPO/scripts"
cp "$ROOT/.githooks/pre-commit" "$REPO/.githooks/"
cp "$ROOT/scripts/validate-frontmatter.sh" "$REPO/scripts/"

skill() {
  mkdir -p "$REPO/$1"
  printf '%s\n' '---' "name: $2" 'description: A sufficiently specific fixture for validation.' '---' > "$REPO/$1/SKILL.md"
}

for category in workflows capabilities mandatory; do
  skill "$category/example-$category" "example-$category"
done
printf '%s\n' 'Initial mandatory documentation.' > "$REPO/mandatory/example-mandatory/README.md"

git -C "$REPO" init -q
git -C "$REPO" config user.email test@example.invalid
git -C "$REPO" config user.name test
git -C "$REPO" add .
git -C "$REPO" commit -qm initial

expect_hook() {
  local expected="$1"
  local output
  if ! output="$(cd "$REPO" && .githooks/pre-commit)"; then
    printf 'FAIL expected hook success, got:\n%s\n' "$output" >&2
    exit 1
  fi
  grep -Fq "$expected" <<< "$output"
}

printf '%s\n' 'Updated mandatory documentation.' > "$REPO/mandatory/example-mandatory/README.md"
git -C "$REPO" add mandatory/example-mandatory/README.md
expect_hook 'validating staged public skill content'
git -C "$REPO" restore --staged mandatory/example-mandatory/README.md
git -C "$REPO" restore mandatory/example-mandatory/README.md

printf '%s\n' '# staged validator comment' >> "$REPO/scripts/validate-frontmatter.sh"
git -C "$REPO" add scripts/validate-frontmatter.sh
expect_hook 'validating staged public skill content'
git -C "$REPO" restore --staged scripts/validate-frontmatter.sh
git -C "$REPO" restore scripts/validate-frontmatter.sh

printf '%s\n' 'Unstaged change.' >> "$REPO/mandatory/example-mandatory/SKILL.md"
printf '\n' >> "$REPO/workflows/example-workflows/SKILL.md"
git -C "$REPO" add workflows/example-workflows/SKILL.md
if output="$(cd "$REPO" && .githooks/pre-commit)"; then
  printf 'FAIL expected hook to reject scoped unstaged changes, got:\n%s\n' "$output" >&2
  exit 1
fi
grep -Fq 'stage or revert scoped unstaged changes before validation' <<< "$output"

git -C "$REPO" restore --staged workflows/example-workflows/SKILL.md
git -C "$REPO" restore workflows/example-workflows/SKILL.md
git -C "$REPO" restore mandatory/example-mandatory/SKILL.md
rm -rf "$REPO/mandatory/example-mandatory"
git -C "$REPO" add -u mandatory/example-mandatory
if output="$(cd "$REPO" && .githooks/pre-commit)"; then
  printf 'FAIL expected hook to reject a deleted required public skill, got:\n%s\n' "$output" >&2
  exit 1
fi
grep -Fq 'mandatory  contains no public SKILL.md files' <<< "$output"

printf '%s\n' 'PASS mandatory and validator trigger paths, deletion, and staged-content guard'
