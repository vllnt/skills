# Clean history for public packages and repositories

## Contract

- Input: A repository or package that is public, or is about to become public, plus any packed or attached release artifacts.
- Output: A pass or fail of the clean-history gate. Findings are reported as rule id or category, commit short-sha, and path only.
- Effects: The scan is read-only. It never rewrites history, force-pushes, or changes visibility. A fail blocks publishing and any visibility flip to public.

### Acceptance

- Full git history on all refs has been scanned with an available history scanner (for example `gitleaks detect --log-opts="--all" --redact`, optionally complemented by `trufflehog git` with no `--since` cutoff).
- Personal and private data have been considered in the current tree and in history: emails other than public or noreply addresses, phone numbers, addresses, private hostnames and tailnet names (for example `*.ts.net`), internal IP addresses, tokens and keys, secret files such as `.env`, private repository names or paths, and customer or other personal data. A current-tree privacy denylist complements the history scan; it does not replace it.
- Packed artifacts (`npm pack --dry-run` and any produced tarball) and hosted release assets have been inspected where they apply.
- Reports contain no secret or personal values.
- On fail: do not publish, and do not make the repository public; if it is not yet public, keep it private. Rotate every discovered secret first. History rewrite or recreating the project as a fresh repository is irreversible and needs an explicit maintainer yes; never force-push without that yes. The preferred clean path for a not-yet-public repository is a new repository with a single clean initial commit, not a rewrite of the existing history.

## Procedure

1. Identify whether the candidate is already public or is about to become public (visibility flip, first public registry publish, new public repository, public mirror, or a later public release). If none of those apply, record the gate as not applicable.
2. Run a full-history scan on all refs. Do not use a `--since` cutoff. If gitleaks is missing, install an official release to `~/.local/bin`. Redact reports.
3. Inspect the current tree and history for the personal and private data categories above, and inspect pack and release artifacts where they apply. This repository's `scripts/privacy-denylist.sh` covers the current tree only.
4. If the gate fails, stop. Keep a not-yet-public repository private. Recommend secret rotation first, then a maintainer decision: prefer a fresh repository with one clean initial commit over a history rewrite. Do not rewrite or force-push without an explicit yes.

## Pitfalls

- A current-tree-only scan is not a full-history scan. Passing `--since` or any cutoff is not a full scan.
- Pattern matches are leads, not proven leaks. No matches do not prove absence.
- Never print secret or personal values into logs, pull requests, or chat. A public CI log is public.
- Already-public repositories still need this gate before every public release, plus a periodic full-history audit.
