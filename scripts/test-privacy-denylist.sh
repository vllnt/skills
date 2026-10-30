#!/usr/bin/env bash
#
# test-privacy-denylist.sh — success and failure paths of privacy-denylist.sh
# in a throwaway repository. Planted values are synthetic.

set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO="$(mktemp -d)"
trap 'rm -rf "$REPO"' EXIT

mkdir -p "$REPO/scripts"
cp "$ROOT/scripts/privacy-denylist.sh" "$REPO/scripts/"
cp "$ROOT/.privacy-denylist" "$ROOT/.privacy-allowlist" "$REPO/"
git -C "$REPO" init -q
git -C "$REPO" config user.email test@example.invalid
git -C "$REPO" config user.name test

failures=0
# check <name> <expected exit> [VAR=value ...]
check() {
  local name="$1" expected="$2"; shift 2
  git -C "$REPO" add -A
  local output status
  output="$(cd "$REPO" && env "$@" bash scripts/privacy-denylist.sh 2>&1)"
  status=$?
  if [[ "$status" != "$expected" ]]; then
    printf 'FAIL %s: expected exit %s, got %s\n%s\n' "$name" "$expected" "$status" "$output" >&2
    failures=$((failures + 1))
    return
  fi
  printf 'OK    %s\n' "$name"
  LAST_OUTPUT="$output"
}

printf 'Plain documentation.\n' > "$REPO/doc.md"
check "clean tree passes" 0 NOOP=1

printf 'host: build-box.example-net.ts.net\n' > "$REPO/doc.md"
check "tailnet hostname fails" 1 NOOP=1
grep -q 'doc.md:1' <<< "$LAST_OUTPUT" || { echo "FAIL hit location not reported" >&2; failures=$((failures + 1)); }
grep -q 'ts.net' <<< "$LAST_OUTPUT" && { echo "FAIL matched content leaked to output" >&2; failures=$((failures + 1)); }

printf 'id 123e4567-e89b-12d3-a456-426614174000\n' > "$REPO/doc.md"
check "uuid fails" 1 NOOP=1

printf 'path /home/someone/project/\n' > "$REPO/doc.md"
check "home path fails" 1 NOOP=1

printf 'mail fixture@example.test\n' > "$REPO/doc.md"
check "allowlisted reserved address passes" 0 NOOP=1

printf 'mail someone@company.io\n' > "$REPO/doc.md"
check "real-looking address fails" 1 NOOP=1

printf 'Plain documentation.\nacme-widget appears here\n' > "$REPO/doc.md"
check "extra pattern from environment fails" 1 'PRIVACY_DENYLIST_EXTRA=acme-widget'
check "invalid extra pattern is an error, not a pass" 2 'PRIVACY_DENYLIST_EXTRA=(unbalanced'
printf 'Plain documentation.\n' > "$REPO/doc.md"
check "extra pattern not present passes" 0 'PRIVACY_DENYLIST_EXTRA=acme-widget'

if (( failures > 0 )); then
  printf '%s failure(s)\n' "$failures" >&2
  exit 1
fi
echo "OK    privacy denylist tests passed"
