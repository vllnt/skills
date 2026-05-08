# Releasing

This repo is designed so AI agents (and humans) can ship a release end-to-end. Three release paths, one source of truth (`CHANGELOG.md`).

## Per-PR (every contribution)

```
1. make change
2. bash scripts/changelog-add.sh "<entry>"   ← appends under [Unreleased]
3. commit                                    ← pre-commit validates frontmatter
4. open PR                                   ← CI blocks if CHANGELOG.md unchanged
                                              or [Unreleased] empty
```

## Three Release Paths

```
┌───────────────────────────────────────────────────────────────────┐
│                    main                                          │
│   ┌──────────────────────────────────────────────────────────┐   │
│   │  PATH A — local script (preferred for fast turnaround)   │   │
│   │  bash scripts/release.sh --bump patch                    │   │
│   │  → bumps, promotes [Unreleased], tags, pushes            │   │
│   │  → publish.yml job `release-from-tag` fires              │   │
│   └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│   ┌──────────────────────────────────────────────────────────┐   │
│   │  PATH B — GitHub Actions UI (workflow_dispatch)          │   │
│   │  Actions tab → Publish → Run workflow → bump=patch/min…  │   │
│   │  → publish.yml job `release-from-dispatch` does the      │   │
│   │    promotion + commit + tag + push                       │   │
│   │  → triggers `release-from-tag` on the resulting tag      │   │
│   └──────────────────────────────────────────────────────────┘   │
│                                                                   │
│   ┌──────────────────────────────────────────────────────────┐   │
│   │  PATH C — canary (automatic on every main push)          │   │
│   │  → publish.yml job `canary` creates                      │   │
│   │    `v<latest-stable>-canary.<sha7>` prerelease           │   │
│   │  → cleaned up automatically when next stable ships       │   │
│   └──────────────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────────────────┘
```

### When to use which path

| Path | Use when | Friction |
|------|----------|----------|
| A — local script | You're already on a clean main locally | Lowest |
| B — workflow_dispatch | You want the bump done from the browser, e.g. on mobile or from another machine | Low |
| C — canary | Always-on. No action needed. Used to grab the latest main as a versioned ref. | None |

## Path A — Local

```bash
bash scripts/release.sh --bump patch    # 0.1.0 -> 0.1.1
bash scripts/release.sh --bump minor    # 0.1.0 -> 0.2.0
bash scripts/release.sh --bump major    # 0.1.0 -> 1.0.0
bash scripts/release.sh --bump patch --dry-run   # preview without pushing
```

What it does:
1. Verifies clean tree on `main`
2. Verifies `[Unreleased]` is non-empty
3. Computes next version from the latest `vX.Y.Z` tag
4. Promotes `[Unreleased]` → `[X.Y.Z] - YYYY-MM-DD`
5. Commits `chore(release): vX.Y.Z`, tags, pushes both

The tag push fires `publish.yml > release-from-tag` which creates the GitHub Release with notes from `CHANGELOG.md`.

## Path B — workflow_dispatch

GitHub UI:

```
Actions  →  Publish  →  Run workflow
  ├─ Branch: main
  └─ bump:   patch | minor | major
```

The workflow runs the same logic as Path A, on the `github-actions[bot]` user, then triggers the tag-driven release job.

## Path C — Canary (automatic)

Every push to `main` (except `chore(release):` commits) gets:

```
v<latest-stable>-canary.<sha7>
```

as a prerelease GitHub Release. Lets agents pin to a specific build of `main` for testing without waiting for a stable cut. Canary tags are deleted automatically when the next stable release lands.

## Frontmatter & changelog gates (BLOCKING)

| Gate | Where | Blocks |
|------|-------|--------|
| Skill frontmatter (`name`, `description`) | `.githooks/pre-commit` + CI `validate-frontmatter` | Commit + merge |
| `CHANGELOG.md` modified in PR | CI `changelog` | Merge |
| `[Unreleased]` non-empty in PR | CI `changelog` | Merge |

## Setup (after clone)

```bash
bash scripts/install-hooks.sh
```

Sets `core.hooksPath=.githooks` so the pre-commit validator runs locally.

## Agent-Friendly Notes

- All scripts are **non-interactive** — no prompts, all flags explicit.
- All scripts are **idempotent where safe** — `changelog-add.sh` won't duplicate identical lines; `release.sh` aborts cleanly on bad state.
- No external dependencies — pure `bash` + `awk` for local; `gh` + `awk` in CI.
- Three independent release paths means no single failure mode blocks shipping.
