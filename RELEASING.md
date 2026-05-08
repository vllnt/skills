# Releasing

This repo is designed so AI agents (and humans) can ship a release end-to-end with two scripts. No manual GitHub UI clicks.

## Flow

```
PR: scripts/changelog-add.sh "<entry>"   ── one entry per PR, BLOCKING in CI
   │
   ▼
main: scripts/release.sh --bump patch    ── bumps version, tags, pushes
   │
   ▼
.github/workflows/publish.yml            ── auto-creates GitHub Release on tag push
```

## Per-PR (every contribution)

1. Make your change.
2. Add a CHANGELOG entry:
   ```bash
   bash scripts/changelog-add.sh --type feat --scope regulatory-guard "add EAA accessibility audit"
   ```
   (or pass a free-form line: `bash scripts/changelog-add.sh "fix(ci): handle empty changelog"`)
3. Commit. The pre-commit hook validates SKILL.md frontmatter for any touched skill.
4. Open PR. CI checks:
   - `validate-frontmatter` — every skill has valid YAML frontmatter
   - `changelog` — `CHANGELOG.md` was modified AND `[Unreleased]` has at least one entry

## Cutting a Release

When you want to ship:

```bash
bash scripts/release.sh --bump patch    # 0.1.0 -> 0.1.1
bash scripts/release.sh --bump minor    # 0.1.0 -> 0.2.0
bash scripts/release.sh --bump major    # 0.1.0 -> 1.0.0

bash scripts/release.sh --bump patch --dry-run    # preview without pushing
```

The script:
1. Verifies clean tree on `main`
2. Verifies `[Unreleased]` is non-empty
3. Computes next version from latest `vX.Y.Z` git tag
4. Promotes `[Unreleased]` → `[X.Y.Z] - YYYY-MM-DD` and prepends a fresh empty `[Unreleased]`
5. Commits `chore(release): vX.Y.Z`, tags `vX.Y.Z`, pushes both

`.github/workflows/publish.yml` then fires on the tag push and creates the GitHub Release with notes extracted from `CHANGELOG.md`.

## Agent-Friendly Notes

- All scripts are **non-interactive** — no prompts, all flags explicit.
- All scripts are **idempotent where safe** — `changelog-add.sh` won't duplicate identical lines; `release.sh` aborts cleanly if state is wrong.
- Errors print to stderr with actionable next steps.
- No external dependencies — pure `bash` + `awk`.

## First-Time Setup (after clone)

```bash
bash scripts/install-hooks.sh
```

Sets `core.hooksPath=.githooks` so the pre-commit validator runs locally.
