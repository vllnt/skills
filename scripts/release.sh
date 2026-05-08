#!/usr/bin/env bash
# DEPRECATED — use scripts/release-prep.sh instead.
# Branch protection on `main` requires release commits to land via a PR.
echo "scripts/release.sh is deprecated."
echo ""
echo "The new flow respects branch protection on main:"
echo "  1) bash scripts/release-prep.sh --bump patch    (opens release PR)"
echo "  2) Squash-merge the PR"
echo "  3) Actions -> Publish -> Run workflow           (creates tag + Release)"
echo ""
echo "See RELEASING.md for the full diagram."
exit 1
