#!/usr/bin/env bash
#
# privacy-denylist.sh — fail when a tracked file matches a denylist pattern
# outside the allowlist.
#
# Patterns (extended regex, one per line, '#' comments; matched case-insensitively):
#   .privacy-denylist          required, tracked, structural patterns only
#   .privacy-denylist.local    optional, untracked, for names that must stay private
#   $PRIVACY_DENYLIST_EXTRA    optional, newline-separated; set it from a CI secret
# Allowlist (.privacy-allowlist): regexes matched against "path:line:token" for each
# matched token, so an allowed token never hides another match on the same line.
#
# Matched content and pattern text are never printed: CI logs of a public
# repository are public.
#
# Exit codes: 0 clean, 1 match found, 2 misuse or invalid pattern.

set -u

cd "$(git rev-parse --show-toplevel)" || exit 2

DENY=.privacy-denylist
ALLOW=.privacy-allowlist
SELF=scripts/privacy-denylist.sh

tracked="$(mktemp)"
extra="$(mktemp)"
patterns="$(mktemp)"
allow_patterns="$(mktemp)"
hits="$(mktemp)"
kept="$(mktemp)"
trap 'rm -f "$tracked" "$extra" "$patterns" "$allow_patterns" "$hits" "$kept"' EXIT

strip() { sed -E '/^[[:space:]]*(#|$)/d'; }

# valid_regexes <file> <label>: every line must compile and must not match the empty string.
valid_regexes() {
  local file="$1" label="$2" n=0 line status
  while IFS= read -r line; do
    n=$((n + 1))
    printf '\n' | grep -qE -e "$line" 2> /dev/null
    status=$?
    if (( status > 1 )); then
      echo "error: $label pattern #$n is not a valid regex" >&2
      return 1
    fi
    if (( status == 0 )); then
      echo "error: $label pattern #$n matches the empty string" >&2
      return 1
    fi
  done < "$file"
}

if [[ ! -f "$DENY" ]]; then
  echo "error: $DENY is required" >&2
  exit 2
fi
strip < "$DENY" > "$tracked"
{
  [[ -f "$DENY.local" ]] && cat "$DENY.local"
  [[ -n "${PRIVACY_DENYLIST_EXTRA:-}" ]] && printf '%s\n' "$PRIVACY_DENYLIST_EXTRA"
} | strip > "$extra"
cat "$tracked" "$extra" > "$patterns"
[[ -f "$ALLOW" ]] && strip < "$ALLOW" > "$allow_patterns"

if [[ ! -s "$tracked" ]]; then
  echo "error: $DENY has no patterns" >&2
  exit 2
fi
valid_regexes "$patterns" "denylist" || exit 2
valid_regexes "$allow_patterns" "allowlist" || exit 2

# -a scans binary files as text; -o reports each matched token on its own line.
git grep -naoiE -f "$patterns" -- . ":(exclude)$DENY" ":(exclude)$ALLOW" ":(exclude)$SELF" > "$hits" 2> /dev/null
status=$?
if (( status > 1 )); then
  echo "error: git grep failed" >&2
  exit 2
fi

if [[ -s "$allow_patterns" ]]; then
  grep -vEf "$allow_patterns" "$hits" > "$kept"
  status=$?
  if (( status > 1 )); then
    echo "error: allowlist filtering failed" >&2
    exit 2
  fi
  mv "$kept" "$hits"
fi

if [[ -s "$hits" ]]; then
  echo "FAIL privacy denylist: $(wc -l < "$hits" | tr -d ' ') match(es); content withheld"
  cut -d: -f1,2 "$hits" | sort -u | sed 's/^/  /'
  exit 1
fi

extra_count="$(wc -l < "$extra" | tr -d ' ')"
if [[ "${CI:-}" == "true" && "$extra_count" == "0" ]]; then
  echo "::warning title=Privacy guard::No private patterns loaded; only the tracked structural patterns were checked."
fi
echo "OK    privacy denylist: no matches ($(wc -l < "$tracked" | tr -d ' ') tracked + $extra_count private patterns)"
