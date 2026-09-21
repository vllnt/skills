#!/usr/bin/env bash
# Exercise the hook against staged content in an isolated repository.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
REPO="$TMP/fixture"

mkdir -p "$REPO/.githooks" "$REPO/scripts"
cp "$ROOT/.githooks/pre-commit" "$REPO/.githooks/"
cp "$ROOT/scripts/validate-frontmatter.sh" "$ROOT/scripts/validate-docs.py" "$ROOT/scripts/bundle-references.py" "$REPO/scripts/"

skill() {
  mkdir -p "$REPO/$1"
  {
    printf '%s\n' '---' "name: $2" 'description: A sufficiently specific fixture for validation.'
    if [[ "$2" == manage-skill ]]; then
      printf '%s\n' 'metadata:' '  internal: true'
    fi
    printf '%s\n' '---'
  } > "$REPO/$1/SKILL.md"
  if [[ "$1" == mandatory/* ]]; then
    printf '%s\n' '## Principles' '' '- A current principle.' >> "$REPO/$1/SKILL.md"
  else
    printf '%s\n' '## Goal' '' 'Produce one result.' '' '### Definition of Done' '' '- One.' '- Two.' '- Three.' '' '## Workflow' '' '1. Work.' >> "$REPO/$1/SKILL.md"
  fi
}

for category in workflows mandatory; do
  skill "$category/example-$category" "example-$category"
done
skill .agents/skills/manage-skill manage-skill
mkdir -p "$REPO/references/capabilities/example" "$REPO/references/protocols"
printf '%s\n' '## Contract' '' '- Input: Scope.' '- Output: Result.' '- Effects: Read-only.' '' '### Acceptance' '' '- One.' '- Two.' '- Three.' '' '## Procedure' '' '1. Work.' > "$REPO/references/capabilities/example/REFERENCE.md"
cp "$REPO/references/capabilities/example/REFERENCE.md" "$REPO/references/protocols/quality-validation.md"
printf '%s\n' '| [example-workflows](workflows/example-workflows/SKILL.md) | A sufficiently specific fixture for validation. |' '| [example-mandatory](mandatory/example-mandatory/SKILL.md) | A sufficiently specific fixture for validation. |' > "$REPO/README.md"
printf '%s\n' '- [example-workflows](workflows/example-workflows/SKILL.md)' '- [example-mandatory](mandatory/example-mandatory/SKILL.md)' > "$REPO/llms.txt"
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

printf '%s\n' 'Additional canonical reference guidance.' >> "$REPO/references/capabilities/example/REFERENCE.md"
git -C "$REPO" add references/capabilities/example/REFERENCE.md
expect_hook 'validating staged public skill content'
git -C "$REPO" restore --staged references/capabilities/example/REFERENCE.md
git -C "$REPO" restore references/capabilities/example/REFERENCE.md

printf '%s\n' 'Staged canonical reference guidance.' >> "$REPO/references/capabilities/example/REFERENCE.md"
git -C "$REPO" add references/capabilities/example/REFERENCE.md
printf '%s\n' 'Unstaged catalog change.' >> "$REPO/README.md"
if output="$(cd "$REPO" && .githooks/pre-commit 2>&1)"; then
  printf 'FAIL expected hook to reject unstaged catalog content, got:\n%s\n' "$output" >&2
  exit 1
fi
grep -Fq 'stage or revert scoped unstaged changes before validation' <<< "$output"
git -C "$REPO" restore --staged references/capabilities/example/REFERENCE.md
git -C "$REPO" restore references/capabilities/example/REFERENCE.md README.md

mkdir -p "$REPO/workflows/example-workflows/references/vstack/capabilities/example"
printf '%s\n' 'Unexpected generated content.' > "$REPO/workflows/example-workflows/references/vstack/capabilities/example/REFERENCE.md"
git -C "$REPO" add workflows/example-workflows/references/vstack/capabilities/example/REFERENCE.md
if output="$(cd "$REPO" && .githooks/pre-commit 2>&1)"; then
  printf 'FAIL expected hook to reject generated reference, got:\n%s\n' "$output" >&2
  exit 1
fi
grep -Fq 'unexpected generated reference' <<< "$output"
git -C "$REPO" restore --staged workflows/example-workflows/references/vstack/capabilities/example/REFERENCE.md
rm -rf "$REPO/workflows/example-workflows/references"

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
