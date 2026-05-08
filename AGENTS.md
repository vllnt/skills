# Agent Instructions — vllnt/skills

> **Sync rule (BLOCKING).** This file (`AGENTS.md`) and `CLAUDE.md` MUST stay byte-identical. CI fails the PR if they drift. When you edit one, edit both. They exist as separate files because some agent runtimes load `AGENTS.md` (open standard) and others load `CLAUDE.md` (Claude Code default) — the content is the same. The CI job that enforces this is `Sync Agent Docs` in `.github/workflows/ci.yml`.

This repo is a collection of agent skills as Markdown files. Compatible with any agent runtime that loads skills from a folder of `<skill>/SKILL.md` documents (Claude Code, OpenCode, Codex, Pi, Cursor, Windsurf, etc.).

## Repo Layout

```
.
├── <skill-name>/
│   ├── SKILL.md          # required, with YAML frontmatter (name, description)
│   ├── README.md         # human-facing docs
│   ├── EXAMPLE.md        # optional usage example
│   └── references/       # on-demand reference docs (don't load eagerly)
├── scripts/              # validate-frontmatter, changelog-add, release-prep, install-hooks
├── .githooks/            # project-managed git hooks (pre-commit)
├── .github/              # workflows, issue/PR templates
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md          # [Unreleased] section is mandatory per PR
├── RELEASING.md          # full release-flow diagram + per-PR + cut-a-release
├── AGENTS.md / CLAUDE.md # ← THIS FILE (kept in sync, see rule above)
└── llms.txt / llms-full.txt
```

## Hard Rules for Contributors (incl. agents)

1. **Every PR must update `CHANGELOG.md`** under `## [Unreleased]`. CI's `Changelog Required` job blocks PRs that don't.
   - Use `bash scripts/changelog-add.sh "<entry>"` to append idempotently.
2. **Every `<skill>/SKILL.md` must have valid YAML frontmatter** with `name` (matching folder) and a `description` ≥20 chars.
   - The pre-commit hook (`scripts/install-hooks.sh` to activate) and CI's `Validate Skill Frontmatter` job both run `scripts/validate-frontmatter.sh`.
3. **Skills must be independent** — no cross-references between skills. Each skill must be usable on its own.
4. **No build step.** Skills are pure Markdown.
5. **`main` is protected. Never push to it directly.** All commits land via squash-merged PR. CI never writes commits to `main`, only tags.
6. **`AGENTS.md` and `CLAUDE.md` must stay identical.** CI's `Sync Agent Docs` job blocks PRs where they differ.

## Adding a New Skill

```
1. mkdir <skill-name>
2. Create <skill-name>/SKILL.md with frontmatter:
   ---
   name: <skill-name>     # must match folder
   description: >=20 chars, specific enough that an agent can route on it
   ---
3. (Optional) <skill-name>/README.md, EXAMPLE.md, references/
4. bash scripts/validate-frontmatter.sh        # local check
5. bash scripts/changelog-add.sh --type feat --scope <skill-name> "initial release"
6. Open PR — squash-merge after CI green
```

## Adding a Change to an Existing Skill

```
1. Edit <skill-name>/...
2. bash scripts/changelog-add.sh --type <feat|fix|docs|chore> --scope <skill-name> "<summary>"
3. Open PR — squash-merge after CI green
```

## Release Flow (PR-driven, no main-writes from CI)

`main` is protected. The flow is designed so branch protection stays on without any PAT or Rulesets bypass actor (mirrors `vllnt/ui`).

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

### `publish.yml` jobs

| Job | Trigger | Action |
|-----|---------|--------|
| `canary` | every push to `main` (except `chore(release):`) | tag + GitHub prerelease `v<latest-stable>-canary.<sha7>` |
| `release-dispatch` | `workflow_dispatch` | creates tag `vX.Y.Z` at `main` HEAD only — no commits pushed |
| `release-from-tag` | any `v*.*.*` tag push | creates GitHub Release from `CHANGELOG.md` section, cleans canaries |

### Cutting a release end-to-end

```bash
bash scripts/release-prep.sh --bump patch    # 0.1.0 -> 0.1.1
# → opens PR release/v0.1.1
# → squash-merge it
# → Actions → Publish → Run workflow on main
# → release-dispatch creates tag v0.1.1
# → release-from-tag publishes the GitHub Release
```

`scripts/release.sh` is a deprecated stub — DO NOT use it. It used to push `chore(release):` directly to `main`, which branch protection now blocks.

### Canary (automatic)

Every merge to `main` (except `chore(release):` commits) auto-publishes `v<latest-stable>-canary.<sha7>` as a GitHub prerelease. Cleaned up automatically when the next stable lands.

See `RELEASING.md` for the long-form version, including dry-run, error cases, and the "why this shape" rationale.

## Style Guide

- Markdown only. No JS/TS code unless inside a skill's example.
- US English, second person ("you do X").
- Each skill's `SKILL.md` description should be specific enough that a routing agent can match on it (don't write "helps with stuff").
- No hidden cross-skill state. Skills are loaded independently.

## Disallowed

- Cross-skill references (`../other-skill/SKILL.md`)
- Hardcoded paths to user systems
- Embedded secrets or credentials
- Auto-fetching remote URLs at skill-load time (load-on-demand only, with the agent's permission)
- Direct pushes to `main`
- `AGENTS.md` and `CLAUDE.md` drifting from each other
