# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

- fix(scripts): changelog-add.sh idempotency check broke when entry started with leading dash
- feat: add scripts/release-prep.sh — opens release PR with version bump and CHANGELOG promotion
- chore(repo): disable wiki and projects, confirm squash-only merge + auto-delete branch on merge, add issue templates
- chore(ci): PR-driven release flow (mirror vllnt/ui): canary on main push + workflow_dispatch tag-only + tag-trigger publish; no main-writes from CI
## [0.1.0] - 2026-05-08

- chore: initial public release of `vllnt/skills`
- feat(regulatory-guard): initial release. Web compliance audit skill covering privacy (GDPR / CCPA / ePrivacy), accessibility (WCAG 2.2 AA / ADA / EAA), consumer & e-commerce (DSA / DMA / CCPA-sale / CAN-SPAM), and AI / content (EU AI Act / copyright / DMCA). Outputs tiered findings with evidence, severity, and remediation steps.
- chore: scaffold MIT license, README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, AGENTS, issue/PR templates, FUNDING, `llms.txt` / `llms-full.txt` for agent discovery.
- chore(ci): three-mode publish workflow — (1) canary tag on every main push, (2) `workflow_dispatch` for stable bumps (patch/minor/major), (3) tag-push trigger for `scripts/release.sh`-driven releases. Auto-extracts release notes from `CHANGELOG.md` and cleans up canary tags after stable.
- chore(ci): require `CHANGELOG.md` update + non-empty `[Unreleased]` on every PR, validate every skill's `SKILL.md` frontmatter on every push and PR.
