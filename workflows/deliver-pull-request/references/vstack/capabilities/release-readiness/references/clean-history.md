# Clean history for public packages and repositories

## Contract

- Input: A repository or package that is public, or is about to become public, plus any packed or attached release artifacts.
- Output: A pass or fail of the clean-history gate. Findings are reported as rule id or category, commit short-sha, and path only.
- Effects: The scan is read-only. It never rewrites history, force-pushes, or changes visibility. A fail blocks publishing and any visibility flip to public.

### Acceptance

- Full git history on all refs has been scanned with an available history scanner (for example `gitleaks detect --log-opts="--all" --redact`, optionally complemented by `trufflehog git` with no `--since` cutoff).
- Personal and private data have been considered in the current tree and in history: emails other than public or noreply addresses, phone numbers, addresses, private hostnames and tailnet names (for example `*.ts.net`), provider VPS hostnames, internal IP addresses, tokens and keys, secret files such as `.env`, private repository names or paths, and customer or other personal data. A current-tree privacy denylist complements the history scan; it does not replace it.
- Commit metadata has been checked: author, committer, and `Co-authored-by` / `Signed-off-by` trailer emails allow only GitHub noreply or bot addresses.
- Packed artifacts (`npm pack --dry-run` and any produced tarball) and hosted release assets have been inspected where they apply.
- Reports contain no secret or personal values.
- On fail: do not publish, and do not make the repository public; if it is not yet public, keep it private. Rotate every discovered secret first. History rewrite or recreating the project as a fresh repository is irreversible and needs an explicit maintainer yes; never force-push without that yes. The preferred clean path for a not-yet-public repository is a new repository with a single clean initial commit, not a rewrite of the existing history.

## Prevention

A clean history is not only a pre-publish scan. These controls must be in place so personal and private data never enter a commit.

- Every commit is authored and committed as the GitHub noreply identity of the committing account (`<id>+<login>@users.noreply.github.com`, resolved with `gh api user --jq '"\(.id)+\(.login)@users.noreply.github.com"'`). Do not leave `user.email` unset: git then records `user@<hostname>`, which can be a provider VPS name.
- Do not put personal emails in `Co-authored-by` or `Signed-off-by` trailers. GitHub squash-merge copies each source commit's author email into a `Co-authored-by` trailer, so a squash is only safe when every source commit already uses a noreply or bot address.
- Do not put private hostnames, provider VPS names, tailnet names, or internal IPs in code, docs, or commit messages.
- Every public repo, and any about to become public, must run a required status check named **Privacy Guard** on pull requests and on pushes. The check covers gitleaks, the commit-metadata email check (PR range on pull requests; full history on a push to the default branch, or `baseline..HEAD` when a committed `.privacy-baseline` is present), and a denylist of private hostname and address patterns (`*.ts.net`, OVH and Hetzner VPS hostnames, RFC1918, tailnet IPs).
- A committed `.privacy-baseline` may name a SHA, a reason, and a decision date so the required commit-metadata check scans only `baseline..HEAD` on push (pull requests still use the PR range). A baseline is allowed only for historical exposure Benoît has accepted, recorded in the security-findings ledger. With no baseline file the required check stays full-history. Repos that use a baseline should also run the optional, non-required weekly full-history audit job (`templates/privacy-guard-history-audit.yml`).
- A local pre-push hook that runs the same email check is optional and recommended. It does not replace the required CI check.
- Maintainers should also turn on GitHub's "Block command line pushes that expose my email" (with "Keep my email addresses private") at the account level. That setting checks only the most recent commit's author email, not trailers, so it does not replace Privacy Guard. It is an account setting; do not change it for someone else.

### Adopting Privacy Guard

Copy these files from this repository into the consuming repo, then add **Privacy Guard** as a required status check on the default branch:

- `references/capabilities/release-readiness/templates/privacy-guard.yml` → `.github/workflows/privacy-guard.yml`
- `scripts/check-commit-emails.sh` (and `scripts/test-check-commit-emails.sh`)
- `scripts/privacy-denylist.sh`, `scripts/test-privacy-denylist.sh`
- `.privacy-denylist`, `.privacy-allowlist`
- Optional: `references/capabilities/release-readiness/templates/pre-push` → `.githooks/pre-push` (enable with `git config core.hooksPath .githooks`)
- Optional, only for accepted historical exposure: `references/capabilities/release-readiness/templates/privacy-baseline.example` → `.privacy-baseline`, and `templates/privacy-guard-history-audit.yml` → `.github/workflows/privacy-guard-history-audit.yml`. Do not make the audit job a required check.

The workflow is generic and contains no personal data. Findings are reported as commit short-sha, field, and category only. The baseline file format is `sha: <40-character commit SHA>`, `reason: <short reason, no personal values>`, and `decided: <YYYY-MM-DD>`, plus `#` comments.

## Procedure

1. Identify whether the candidate is already public or is about to become public (visibility flip, first public registry publish, new public repository, public mirror, or a later public release). If none of those apply, record the gate as not applicable.
2. Run a full-history scan on all refs. Do not use a `--since` cutoff. If gitleaks is missing, install an official release to `~/.local/bin`. Redact reports.
3. Inspect the current tree and history for the personal and private data categories above, inspect commit author, committer, and trailer emails, and inspect pack and release artifacts where they apply. This repository's `scripts/privacy-denylist.sh` covers the current tree only; `scripts/check-commit-emails.sh` covers commit metadata (the pull-request range, or on a push the range after a committed `.privacy-baseline`, or the full history when no baseline is present).
4. If the gate fails, stop. Keep a not-yet-public repository private. Recommend secret rotation first, then a maintainer decision: prefer a fresh repository with one clean initial commit over a history rewrite. Do not rewrite or force-push without an explicit yes.

## Pitfalls

- A current-tree-only scan is not a full-history scan. Passing `--since` or any cutoff is not a full scan. Checking only author and committer emails is not enough: squash-merge trailers are a leak path.
- Pattern matches are leads, not proven leaks. No matches do not prove absence.
- Never print secret or personal values into logs, pull requests, or chat. A public CI log is public.
- Already-public repositories still need this gate before every public release, plus a periodic full-history audit.
