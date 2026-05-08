# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

- fix(ci): Changelog Required job no longer false-fails on release PRs (release/v* branches intentionally empty [Unreleased] when promoting to a version)
- fix(ci): release-dispatch now creates tag + GitHub Release + cleans canaries in one job (tags pushed by GITHUB_TOKEN don't cascade-trigger workflows). release-from-tag kept as idempotent fallback for manually-pushed tags.
- docs: add Codex + Pi to "Compatible with" lists in README, AGENTS, CLAUDE, llms.txt

## [0.1.0] - 2026-05-08

- chore: initial public release of `vllnt/skills`.
- feat(regulatory-guard): initial release. Web compliance audit skill covering privacy (GDPR / CCPA / ePrivacy), accessibility (WCAG 2.2 AA / ADA / EAA), consumer & e-commerce (DSA / DMA / CCPA-sale / CAN-SPAM), and AI / content (EU AI Act / copyright / DMCA). Outputs tiered findings with evidence, severity, and remediation steps.
- chore: scaffold MIT license, README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, AGENTS, issue/PR templates, FUNDING, `llms.txt` / `llms-full.txt` for agent discovery.
- chore(agents): add `CLAUDE.md` byte-identical mirror of `AGENTS.md`. Document the sync rule in both files; enforce via the `Sync Agent Docs` CI job AND a pre-commit drift guard.
- feat(scripts): `scripts/release-prep.sh` — opens a release PR with version bump and `[Unreleased]` → `[X.Y.Z]` promotion. Replaces the old direct-push-to-main flow.
- fix(scripts): `scripts/changelog-add.sh` idempotency check failed when an entry started with `-` (grep parsed it as an option). Added `--` separator.
- chore(ci): PR-driven release pipeline — `canary` on every main push, `release-dispatch` (`workflow_dispatch`) creates the tag at main HEAD only, `release-from-tag` extracts notes from `CHANGELOG.md` and cleans canary tags. CI never writes commits to `main`. Mirrors `vllnt/ui`.
- chore(ci): require `CHANGELOG.md` update + non-empty `[Unreleased]` + valid skill frontmatter + `AGENTS.md` ≡ `CLAUDE.md` on every PR. All four are required status checks on `main`.
- chore(repo): squash-only merging, auto-delete branch on merge, wiki disabled, projects disabled, discussions disabled.
