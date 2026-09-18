#!/usr/bin/env bash
#
# validate-frontmatter.sh
#
# Verifies this collection's required public categories each contain skills with
# valid YAML frontmatter. It also rejects duplicate names across categories,
# because flat runtime installation would make those entries ambiguous.
# Each SKILL.md requires at minimum:
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
categories=(workflows mandatory)
names_file="$(mktemp "${TMPDIR:-/tmp}/vllnt-skills-names.XXXXXX")"
trap 'rm -f "$names_file"' EXIT

trim() {
  local value="$1"
  value="${value#"${value%%[![:space:]]*}"}"
  value="${value%"${value##*[![:space:]]}"}"
  printf '%s' "$value"
}

# Accept the collection's supported frontmatter subset: a flat mapping of
# single-line strings. Block, collection, alias, tag, and nested values need a
# YAML parser and are intentionally unsupported here.
scalar_value() {
  local value normalized
  value="$(trim "$1")"
  normalized="$(printf '%s' "$value" | tr '[:upper:]' '[:lower:]')"

  case "$value" in
    ''|'|'*|'>'*|'['*|'{'*|'&'*|'!'*|\**|'#'* ) return 1 ;;
  esac
  case "$normalized" in
    null|'~'|true|false|yes|no|on|off) return 1 ;;
  esac

  if [[ "$value" == \"* ]]; then
    [[ "$value" == *\" && "${#value}" -ge 2 ]] || return 1
    value="${value:1:${#value}-2}"
  elif [[ "$value" == \'* ]]; then
    [[ "$value" == *\' && "${#value}" -ge 2 ]] || return 1
    value="${value:1:${#value}-2}"
  elif [[ "$value" == *\" || "$value" == *\' || "$value" == *': '* ]]; then
    return 1
  fi

  [[ -n "$value" ]] || return 1
  printf '%s' "$value"
}

for category in "${categories[@]}"; do
  if [[ ! -d "$category" ]]; then
    echo "FAIL  $category  missing required public category directory"
    errors=$((errors + 1))
    continue
  fi

  category_checked=0
  while IFS= read -r skill_md; do
    category_checked=$((category_checked + 1))
  checked=$((checked + 1))
  skill_dir="$(basename "$(dirname "$skill_md")")"

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
  if ! block="$(awk 'BEGIN{in_fm=0; closed=0}
                NR==1 && /^---[[:space:]]*$/ { in_fm=1; next }
                in_fm && /^---[[:space:]]*$/ { closed=1; exit }
                in_fm { print }
                END { if (!closed) exit 1 }' "$skill_md")"; then
    echo "FAIL  $skill_md  frontmatter block missing or unterminated"
    errors=$((errors + 1))
    continue
  fi

  if [[ -z "$block" ]]; then
    echo "FAIL  $skill_md  frontmatter block missing or unterminated"
    errors=$((errors + 1))
    continue
  fi

  header_names_file="$(mktemp "${TMPDIR:-/tmp}/vllnt-skills-header.XXXXXX")"
  while IFS= read -r header_line; do
    [[ -z "$header_line" ]] && continue
    if [[ ! "$header_line" =~ ^[A-Za-z][A-Za-z0-9_-]*:[[:space:]]*.*$ ]]; then
      echo "FAIL  $skill_md  frontmatter must be a flat mapping of single-line strings"
      errors=$((errors + 1))
      continue
    fi

    header_name="${header_line%%:*}"
    header_raw="${header_line#*:}"
    if ! scalar_value "$header_raw" >/dev/null; then
      echo "FAIL  $skill_md  frontmatter field '$header_name' must be a non-empty scalar string"
      errors=$((errors + 1))
    fi
    if grep -Fxq "$header_name" "$header_names_file"; then
      echo "FAIL  $skill_md  duplicate frontmatter field '$header_name'"
      errors=$((errors + 1))
    else
      printf '%s\n' "$header_name" >> "$header_names_file"
    fi
  done <<< "$block"
  rm -f "$header_names_file"

  name_lines="$(printf '%s\n' "$block" | grep -E '^name:[[:space:]]*' || true)"
  desc_lines="$(printf '%s\n' "$block" | grep -E '^description:[[:space:]]*' || true)"
  name_count="$(printf '%s\n' "$name_lines" | sed '/^$/d' | wc -l | tr -d ' ')"
  desc_count="$(printf '%s\n' "$desc_lines" | sed '/^$/d' | wc -l | tr -d ' ')"
  name_raw="$(printf '%s\n' "$name_lines" | head -n1 | sed -E 's/^name:[[:space:]]*//')"
  desc_raw="$(printf '%s\n' "$desc_lines" | head -n1 | sed -E 's/^description:[[:space:]]*//')"
  name_val="$(scalar_value "$name_raw" || true)"
  desc_val="$(scalar_value "$desc_raw" || true)"

  if [[ "$name_count" != "1" || -z "$name_val" ]]; then
    echo "FAIL  $skill_md  name must be one non-empty scalar string"
    errors=$((errors + 1))
  elif [[ "$name_val" != "$skill_dir" ]]; then
    echo "FAIL  $skill_md  name='$name_val' does not match folder '$skill_dir'"
    errors=$((errors + 1))
  else
    printf '%s\t%s\n' "$name_val" "$skill_md" >> "$names_file"
  fi

  if [[ "$desc_count" != "1" || -z "$desc_val" ]]; then
    echo "FAIL  $skill_md  description must be one non-empty scalar string"
    errors=$((errors + 1))
  elif [[ "${#desc_val}" -lt 20 ]]; then
    echo "FAIL  $skill_md  description too short (<20 chars) — be specific so agents can route"
    errors=$((errors + 1))
  fi
  done < <(find "$category" -mindepth 2 -maxdepth 2 -type f -name 'SKILL.md' -print | sort)

  if [[ "$category_checked" -eq 0 ]]; then
    echo "FAIL  $category  contains no public SKILL.md files"
    errors=$((errors + 1))
  fi
done

while IFS=$'\t' read -r duplicate_name duplicate_paths; do
  [[ -n "$duplicate_name" ]] || continue
  echo "FAIL  duplicate public skill name '$duplicate_name' across categories: $duplicate_paths"
  errors=$((errors + 1))
done < <(awk -F '\t' '
  { paths[$1] = paths[$1] ? paths[$1] ", " $2 : $2; count[$1]++ }
  END { for (name in count) if (count[name] > 1) print name "\t" paths[name] }
' "$names_file" | sort)

if [[ "$errors" -gt 0 ]]; then
  echo ""
  echo "Frontmatter validation FAILED: $errors error(s) across $checked skill(s)"
  exit 1
fi

echo "OK    $checked skill(s) validated"
exit 0
