#!/usr/bin/env bash
#
# privacy-denylist.sh — fail when a tracked file matches a denylist pattern
# outside the allowlist.
#
# Patterns (extended regex, one per line, '#' comments):
#   .privacy-denylist          tracked, structural patterns only
#   .privacy-denylist.local    optional, untracked, for names that must stay private
#   $PRIVACY_DENYLIST_EXTRA    optional, newline-separated; set it from a CI secret
# Allowlist (.privacy-allowlist): regexes matched against "path:line:content" of a hit.
#
# Matched content is never printed: CI logs of a public repository are public.
#
# Exit codes: 0 clean, 1 match found, 2 misuse or bad pattern.

set -u

cd "$(git rev-parse --show-toplevel)" || exit 2

DENY=.privacy-denylist
ALLOW=.privacy-allowlist
SELF=scripts/privacy-denylist.sh

patterns="$(mktemp)"
allow_patterns="$(mktemp)"
hits="$(mktemp)"
trap 'rm -f "$patterns" "$allow_patterns" "$hits"' EXIT

strip() { sed -E '/^[[:space:]]*(#|$)/d'; }

{
  for f in "$DENY" "$DENY.local"; do [[ -f "$f" ]] && cat "$f"; done
  [[ -n "${PRIVACY_DENYLIST_EXTRA:-}" ]] && printf '%s\n' "$PRIVACY_DENYLIST_EXTRA"
} | strip > "$patterns"
[[ -f "$ALLOW" ]] && strip < "$ALLOW" > "$allow_patterns"

if [[ ! -s "$patterns" ]]; then
  echo "error: no denylist patterns found; expected $DENY" >&2
  exit 2
fi

git grep -nIiE -f "$patterns" -- . ":(exclude)$DENY" ":(exclude)$ALLOW" ":(exclude)$SELF" > "$hits"
status=$?
if (( status > 1 )); then
  echo "error: git grep failed; check the denylist patterns" >&2
  exit 2
fi

if [[ -s "$allow_patterns" ]]; then
  grep -vEf "$allow_patterns" "$hits" > "$hits.kept"
  mv "$hits.kept" "$hits"
fi

if [[ -s "$hits" ]]; then
  echo "FAIL privacy denylist: $(wc -l < "$hits" | tr -d ' ') match(es); content withheld"
  cut -d: -f1,2 "$hits" | sort -u | sed 's/^/  /'
  exit 1
fi

echo "OK    privacy denylist: no matches ($(wc -l < "$patterns" | tr -d ' ') patterns)"
