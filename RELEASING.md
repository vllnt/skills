# Releasing

`main` is protected. No commits land on `main` outside a squash-merged PR. CI never pushes commits to `main`. The release flow respects this.

## Per-PR (every contribution)

```
1. make change
2. bash scripts/changelog-add.sh "<entry>"   appends under [Unreleased]
3. commit                                    pre-commit validates frontmatter
4. open PR                                   CI blocks if CHANGELOG unchanged
                                              or [Unreleased] empty
```

CI gates that block the merge:
- `Validate Skill Frontmatter` — every `<skill>/SKILL.md` has valid YAML frontmatter
- `Changelog Required` — `CHANGELOG.md` modified AND `[Unreleased]` has at least one bullet

## At-a-glance

```
        ┌──────────────────────────────────────────┐
        │         Cutting a release                │
        │  bash scripts/release-prep.sh --bump pX  │
        │  → opens PR `release/vX.Y.Z` promoting   │
        │    [Unreleased] -> [X.Y.Z] - YYYY-MM-DD  │
        └─────────────────┬────────────────────────┘
                          │ squash-merge release PR
                          ▼
        ┌──────────────────────────────────────────┐
        │ Actions → Publish → Run workflow         │
        │  → reads version from CHANGELOG          │
        │  → creates tag vX.Y.Z at main HEAD       │
        │    (tags bypass branch protection)       │
        │  → release-from-tag: GitHub Release      │
        │    with notes from CHANGELOG, cleans     │
        │    canary tags                           │
        └──────────────────────────────────────────┘
```

## Three jobs in `publish.yml`

| Job | Trigger | Action |
|-----|---------|--------|
| `canary` | every push to `main` (except `chore(release):`) | tag + GitHub prerelease `v<latest-stable>-canary.<sha7>` |
| `release-dispatch` | `workflow_dispatch` | creates tag `vX.Y.Z` at `main` HEAD only — no commits pushed |
| `release-from-tag` | any `v*.*.*` tag push | creates GitHub Release from `CHANGELOG.md` section, cleans canaries |

`release-dispatch` deliberately pushes only the tag — branch protection stays intact and no PAT or bypass actor is needed (mirrors `vllnt/ui`'s pattern).

## Cutting a Release

```bash
bash scripts/release-prep.sh --bump patch    # 0.1.0 -> 0.1.1
bash scripts/release-prep.sh --bump minor
bash scripts/release-prep.sh --bump major
bash scripts/release-prep.sh --bump patch --dry-run    # preview, no branch/PR
```

What it does (no force-push, no main-write):
1. Verifies clean main + non-empty `[Unreleased]`
2. Computes next version from latest `vX.Y.Z` tag
3. Creates branch `release/vX.Y.Z`, promotes `[Unreleased]` → `[X.Y.Z] - YYYY-MM-DD`
4. Pushes branch + opens PR

Squash-merge the release PR. Then **Actions → Publish → Run workflow** on `main`. The `release-dispatch` job creates the tag, which fires `release-from-tag` — your GitHub Release lands with notes auto-extracted from `CHANGELOG.md`.

## Canary (automatic)

Every push to `main` (except `chore(release):` commits) creates `v<latest-stable>-canary.<sha7>` as a GitHub prerelease. Lets agents pin to a specific main build. Canary tags are cleaned up automatically when the next stable lands.

## Setup (after clone)

```bash
bash scripts/install-hooks.sh
```

Sets `core.hooksPath=.githooks` so the pre-commit validator runs locally.

## Why this shape

- **Branch protection always-on.** No PAT, no Rulesets bypass actor needed. Every commit on main went through CI + a squash-merged PR.
- **CI never touches main directly.** Only tags. Tags don't trigger required status checks, so they can be created from `GITHUB_TOKEN` even with `enforce_admins=true`.
- **Release notes come from one source of truth.** Whatever is in `CHANGELOG.md`'s `[X.Y.Z]` section becomes the GitHub Release body — no separate "release notes" doc to drift.
- **Canary every push.** Frees you from waiting on stable cuts to test main.

## Agent-Friendly Notes

- All scripts are non-interactive (flags only).
- All scripts are idempotent where safe.
- No external deps — `bash` + `awk` + `gh`.
- Three independent paths (canary / dispatch / tag) means no single failure mode blocks shipping.
