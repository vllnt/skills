---
name: improve-code
description: Simplify code and comments while preserving observable contracts and affected consumers.
---

## Goal

Reduce demonstrated maintenance cost while preserving supported behavior, or return an assessment of proposed changes and checks.

### Definition of Done

- Maintenance cost, preserved contracts, callers, and relevant failures are identified.
- Assessment returns candidates and checks without transformations or execution.
- An authorized change is minimal and has before/after caller evidence.
- Unverified transformations and remaining risk are explicit.
- Current validation accepts the selected mode; an unmet required criterion remains REVISE or BLOCKED.

## Workflow

1. Resolve maintenance cost, contracts, scope, mode, and evidence from consumer rules and configuration. Inspect application, test, build, deployment, and recovery consumers before declaring code unused.
2. Establish an authorized baseline. When architecture, test coverage, runtime performance, or a workspace boundary is in scope, use [Code architecture](references/vstack/capabilities/code-architecture/REFERENCE.md), [Code test management](references/vstack/capabilities/code-test-management/REFERENCE.md), [Runtime performance](references/vstack/capabilities/runtime-performance/REFERENCE.md), or [Workspace Turborepo](references/vstack/capabilities/workspace-turborepo/REFERENCE.md) with the mode, scope, candidate, and evidence; in assessment mode, inspect criteria and propose checks only. Prefer deletion or existing interfaces. Rank candidates by demonstrated benefit and preservation risk; drop cosmetic churn and consolidate overlapping work.
3. In change mode, make the smallest authorized transformation while preserving dependency direction, validation, errors, documentation, and unique test protection.
4. In change mode, exercise affected real callers before and after, including applicable success, failure, denial, compatibility, packaging, and build behavior.
5. Before reporting substantive work, validate the change or ranked assessment shortlist through [Quality validation](references/vstack/protocols/quality-validation.md), passing mode, scope, candidate, and evidence. If unavailable, self-assess, obtain independent review and critique, repair within mode, and renew affected checks and verdicts.
