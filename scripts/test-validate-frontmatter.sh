#!/usr/bin/env bash
# Exercise discovery and validation in an isolated repository; never modify real skills.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
REPO="$TMP/fixture repo"
mkdir -p "$REPO/scripts"
cp "$ROOT/scripts/validate-frontmatter.sh" "$REPO/scripts/"

skill() {
  mkdir -p "$REPO/$1"
  printf '%s\n' '---' "name: $2" 'description: A sufficiently specific fixture for validation.' '---' > "$REPO/$1/SKILL.md"
}

expect_count() {
  local output
  output="$(bash "$REPO/scripts/validate-frontmatter.sh")"
  if ! grep -q "^OK    $1 skill(s) validated$" <<< "$output"; then
    printf 'FAIL expected %s skill(s), got:\n%s\n' "$1" "$output" >&2
    exit 1
  fi
}

expect_failure() {
  local output
  if output="$(bash "$REPO/scripts/validate-frontmatter.sh")"; then
    printf 'FAIL expected validation error, got:\n%s\n' "$output" >&2
    exit 1
  fi
  grep -Fq "$1" <<< "$output"
}

# The collection requires both public categories and at least one entry in
# each. An individual runtime may install a subset, but this validator guards
# the collection source tree.
expect_failure "missing required public category directory"

for category in workflows mandatory; do
  skill "$category/example-$category" "example-$category"
done
expect_count 2

mv "$REPO/mandatory/example-mandatory" "$REPO/held-mandatory"
expect_failure "mandatory  contains no public SKILL.md files"
mv "$REPO/held-mandatory" "$REPO/mandatory/example-mandatory"
expect_count 2

# Only the two public categories are in scope.
skill outside outside
skill other/example example
skill .agents/skills/manage-skill manage-skill
expect_count 2

# Ignore internal files even when they resemble skills.
for ignored in .git .github .githooks .worktrees .pi scripts node_modules specs docs references coverage dist; do
  skill "$ignored/ignored" wrong-name
done
expect_count 2

skill workflows/bad wrong-name
expect_failure "does not match folder 'bad'"
skill workflows/bad bad
printf '%s\n' '---' 'name: bad' 'description: short' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure 'description too short'
printf '%s\n' '---' 'name: {}' 'description: A sufficiently specific fixture for validation.' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure 'name must be one non-empty scalar string'
printf '%s\n' '---' 'name: bad' 'description: []' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure 'description must be one non-empty scalar string'
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' > "$REPO/workflows/bad/SKILL.md"
expect_failure 'frontmatter block missing or unterminated'
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'broken: [' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "frontmatter field 'broken' must be a non-empty scalar string"
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' '- item' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure 'frontmatter must be a flat mapping of single-line strings'
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'license: MIT' 'license: Apache-2.0' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "duplicate frontmatter field 'license'"
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'license: "unterminated' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "frontmatter field 'license' must be a non-empty scalar string"
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'license: *shared' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "frontmatter field 'license' must be a non-empty scalar string"
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'license: !custom MIT' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "frontmatter field 'license' must be a non-empty scalar string"
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'license: MIT: nested' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "frontmatter field 'license' must be a non-empty scalar string"
printf '%s\n' '---' 'name: bad' 'description: # This long comment is not a string value.' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "frontmatter field 'description' must be a non-empty scalar string"
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'license: null' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "frontmatter field 'license' must be a non-empty scalar string"
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'license: ~' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "frontmatter field 'license' must be a non-empty scalar string"
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'license: TRUE' '---' > "$REPO/workflows/bad/SKILL.md"
expect_failure "frontmatter field 'license' must be a non-empty scalar string"
printf '%s\n' '# Missing frontmatter' > "$REPO/workflows/bad/SKILL.md"
expect_failure "missing opening '---'"
skill workflows/bad bad
expect_count 3
printf '%s\n' '---' 'name: bad' 'description: A sufficiently specific fixture for validation.' 'license: MIT' '---' > "$REPO/workflows/bad/SKILL.md"
expect_count 3

skill mandatory/example-workflows example-workflows
expect_failure "duplicate public skill name 'example-workflows' across categories"
rm -rf "$REPO/mandatory/example-workflows"
expect_count 3

printf '%s\n' 'PASS required categories, multi-entry discovery, ignored directories, duplicate names, invalid frontmatter, and recovery'
