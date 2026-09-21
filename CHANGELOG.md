# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

- refactor(review): make reviewer coverage proportional, capability-aware, and incremental
- Document manual notification resends and distinguish successful delivery from a verified downstream merge.
- Document canonical skill ownership, multi-host distribution, and the protected automatic-update boundary.
- Notify Vstack distribution after main updates through a fixed cross-repository event, with fail-closed credential checks and regression tests.
- fix(delivery): require current project-defined local checks before issue-delivery pushes and PR writes or repair pushes
- Fix root Skills CLI discovery by excluding the repository-local maintainer with internal metadata; validate the exclusion and test public discovery.
- refactor: distribute internal procedures as on-demand workflow references, keeping only workflows and principles discoverable
- Adopt family-specific agent-facing templates across every skill and the local maintainer; validate structure and strengthen evidence, effect boundaries, and targeted failure handling.

- Share upfront quality criteria, self-assessment, independent review/critique, and renewed acceptance across substantive workflows and skill maintenance.

- Organize Vstack skills into user workflows, internal capabilities, and three lightweight session principles for thinking, orchestration, and collaboration.
- Drive tasks to their requested endpoint with proportional independent review, reusable evidence, explicit decisions, and bounded recovery loops.
- Add project creation/alignment and live `@vllnt` package discovery, including compatible stable/canary evidence; document the optional Vstack profile.
- Add infrastructure posture review and cost modeling; distinguish complete assessments from unverified target behavior.
- Simplify issue, roadmap, architecture, compliance, landing-page, and release references; preserve consumer policy and standalone skill use.
- Align UI/platform checks, test evidence, prototypes, planning, and PR completion criteria with their requested modes.
- Strengthen catalog validation and failure-path fixtures; refresh public navigation, maintenance rules, evaluation cases, and publication hygiene.

## [0.1.1] - 2026-05-08

- fix(ci): Changelog Required job no longer false-fails on release PRs (release/v* branches intentionally empty [Unreleased] when promoting to a version)
- fix(ci): release-dispatch now creates tag + GitHub Release + cleans canaries in one job (tags pushed by GITHUB_TOKEN don't cascade-trigger workflows). release-from-tag kept as idempotent fallback for manually-pushed tags.
- docs: add Codex + Pi to "Compatible with" lists in collection documentation

## [0.1.0] - 2026-05-08

- chore: initial public release of `vllnt/skills`.
- feat: initial web compliance skill. Web compliance audit skill covering privacy (GDPR / CCPA / ePrivacy), accessibility (WCAG 2.2 AA / ADA / EAA), consumer & e-commerce (DSA / DMA / CCPA-sale / CAN-SPAM), and AI / content (EU AI Act / copyright / DMCA). Outputs tiered findings with evidence, severity, and remediation steps.
- chore: scaffold MIT license, README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, AGENTS, issue/PR templates, FUNDING, `llms.txt` for agent discovery.
- feat(scripts): `scripts/release-prep.sh` — opens a release PR with version bump and `[Unreleased]` → `[X.Y.Z]` promotion.
- fix(scripts): `scripts/changelog-add.sh` idempotency check failed when an entry started with `-` (grep parsed it as an option). Added `--` separator.
- chore(ci): PR-driven release pipeline — `canary` on every main push, `release-dispatch` (`workflow_dispatch`) creates the tag at main HEAD only, `release-from-tag` extracts notes from `CHANGELOG.md` and cleans canary tags. CI never writes commits to `main`. Mirrors `vllnt/ui`.
- chore(ci): require `CHANGELOG.md` update + non-empty `[Unreleased]` + valid skill frontmatter on every PR.
- chore(repo): squash-only merging, auto-delete branch on merge, wiki disabled, projects disabled, discussions disabled.
