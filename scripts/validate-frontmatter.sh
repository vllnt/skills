#!/usr/bin/env bash
#
# validate-frontmatter.sh
#
# Verifies every <skill>/SKILL.md has valid YAML frontmatter with at minimum:
#   - name        (string, matches folder name)
#   - description (string, non-empty, single line)
#
# Run locally: bash scripts/validate-frontmatter.sh
# Wired into:  .githooks/pre-commit  +  .github/workflows/ci.yml
#
# Exit codes: 0 OK, 1 validation error, 2 misuse.

set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 2

errors=0
checked=0

# Skip these top-level dirs when looking for skills.
SKIP_RE='^(\.git|\.github|\.githooks|\.worktrees|scripts|node_modules|specs|docs|coverage|dist)$'

while IFS= read -r skill_md; do
  # Path looks like "./<skill>/SKILL.md" or "./<skill>/<sub>/SKILL.md".
  rel="${skill_md#./}"
  top="${rel%%/*}"
  if [[ "$top" =~ $SKIP_RE ]]; then
    continue
  fi

  # Only validate top-level skill directories: <skill>/SKILL.md
  depth=$(awk -F'/' '{print NF}' <<< "$rel")
  if [[ "$depth" -ne 2 ]]; then
    continue
  fi

  checked=$((checked + 1))
  skill_dir="$top"

  # Read file once.
  content="$(cat "$skill_md")"

  # Must start with '---' on line 1.
  first_line="$(printf '%s\n' "$content" | head -n1)"
  if [[ "$first_line" != "---" ]]; then
    echo "FAIL  $skill_md  missing opening '---' frontmatter delimiter"
    errors=$((errors + 1))
    continue
  fi

  # Extract block between first and second '---'.
  block="$(awk 'BEGIN{in_fm=0; closed=0}
                NR==1 && /^---[[:space:]]*$/ { in_fm=1; next }
                in_fm && /^---[[:space:]]*$/ { closed=1; exit }
                in_fm { print }
                END { if (!closed) exit 1 }' "$skill_md")"

  if [[ -z "$block" ]]; then
    echo "FAIL  $skill_md  frontmatter block missing or unterminated"
    errors=$((errors + 1))
    continue
  fi

  name_val="$(printf '%s\n' "$block" | grep -E '^name:[[:space:]]*' | head -n1 | sed -E 's/^name:[[:space:]]*//; s/^"//; s/"$//; s/^'"'"'//; s/'"'"'$//')"
  desc_val="$(printf '%s\n' "$block" | grep -E '^description:[[:space:]]*' | head -n1 | sed -E 's/^description:[[:space:]]*//')"

  if [[ -z "$name_val" ]]; then
    echo "FAIL  $skill_md  missing required field: name"
    errors=$((errors + 1))
  elif [[ "$name_val" != "$skill_dir" ]]; then
    echo "FAIL  $skill_md  name='$name_val' does not match folder '$skill_dir'"
    errors=$((errors + 1))
  fi

  if [[ -z "$desc_val" ]]; then
    echo "FAIL  $skill_md  missing required field: description"
    errors=$((errors + 1))
  elif [[ "${#desc_val}" -lt 20 ]]; then
    echo "FAIL  $skill_md  description too short (<20 chars) — be specific so agents can route"
    errors=$((errors + 1))
  fi

done < <(find . -maxdepth 2 -type f -name 'SKILL.md' 2>/dev/null)

if [[ "$checked" -eq 0 ]]; then
  echo "WARN  no SKILL.md files found at depth=2 — nothing to validate"
fi

if [[ "$errors" -gt 0 ]]; then
  echo ""
  echo "Frontmatter validation FAILED: $errors error(s) across $checked skill(s)"
  exit 1
fi

echo "OK    $checked skill(s) validated"
exit 0
