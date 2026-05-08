# Agent Instructions — vllnt/skills

This repo is a collection of agent skills as Markdown files. Compatible with any agent runtime that loads skills from a folder of `<skill>/SKILL.md` documents (Claude Code, OpenCode, Cursor, Windsurf, etc.).

## Repo Layout

```
.
├── <skill-name>/
│   ├── SKILL.md          # required, with YAML frontmatter (name, description)
│   ├── README.md         # human-facing docs
│   ├── EXAMPLE.md        # optional usage example
│   └── references/       # on-demand reference docs (don't load eagerly)
├── scripts/              # shell scripts: validate, changelog, release
├── .githooks/            # project-managed git hooks (pre-commit)
├── .github/              # workflows, issue/PR templates
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md          # [Unreleased] section is mandatory per PR
├── RELEASING.md          # release flow for agents
└── llms.txt / llms-full.txt
```

## Hard Rules for Contributors (incl. agents)

1. **Every PR must update `CHANGELOG.md`** under `## [Unreleased]`. CI blocks PRs that don't.
   - Use `bash scripts/changelog-add.sh "<entry>"` to append idempotently.
2. **Every `<skill>/SKILL.md` must have valid YAML frontmatter** with `name` (matching folder) and a `description` ≥20 chars.
   - The pre-commit hook (`scripts/install-hooks.sh` to activate) and CI both run `scripts/validate-frontmatter.sh`.
3. **Skills must be independent** — no cross-references between skills. Each skill must be usable on its own.
4. **No build step.** Skills are pure Markdown.
5. **Releases are scripted.** Don't tag manually. Run `bash scripts/release.sh --bump <patch|minor|major>` on `main`. The publish workflow turns the tag into a GitHub Release using the changelog body.

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
6. Open PR
```

## Adding a Change to an Existing Skill

```
1. Edit <skill-name>/...
2. bash scripts/changelog-add.sh --type <feat|fix|docs|chore> --scope <skill-name> "<summary>"
3. Open PR
```

## Releasing

See [RELEASING.md](./RELEASING.md). One command on `main`:

```bash
bash scripts/release.sh --bump patch
```

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
