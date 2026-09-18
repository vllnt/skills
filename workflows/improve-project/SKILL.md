---
name: improve-project
description: Adapt an existing repository to applicable stack preferences through small verified stages.
---

## Goal

Realign an established project with applicable stack preferences in small verified stages, or return its staged plan.

### Definition of Done

- Alignment, preserved contracts, package/runtime choices, and stage boundary are explicit.
- A plan contains stages, acceptance, recovery, and gaps without execution or data changes.
- An authorized stage has configuration and behavior evidence or a labeled platform gap.
- Data transitions have required recovery and authorization evidence.
- Current validation accepts the selected mode; an unmet required criterion remains REVISE or BLOCKED.

## Workflow

1. Resolve target alignment, current state, rules, authority, preserved contracts, replacement scope, criteria, and proof.
2. When alignment or package choices are in scope, use [Project alignment](references/vstack/capabilities/project-alignment/REFERENCE.md) and [Stack packages](references/vstack/capabilities/stack-packages/REFERENCE.md) with the mode, scope, candidate, and evidence. For a selected [TypeScript](references/vstack/capabilities/typescript-configuration/REFERENCE.md), [ESLint](references/vstack/capabilities/eslint-configuration/REFERENCE.md), [workspace](references/vstack/capabilities/workspace-turborepo/REFERENCE.md), [Convex](references/vstack/capabilities/convex-components/REFERENCE.md), [CI](references/vstack/capabilities/ci-optimization/REFERENCE.md), or [performance](references/vstack/capabilities/runtime-performance/REFERENCE.md) concern, use that reference; in planning, inspect criteria and propose checks only. Otherwise compare consumer evidence, exports, peers, data owners, and compatibility directly. Define the smallest stage.
3. In change mode, capture an authorized baseline, then apply one authorized stage with exact dependency and configuration checks.
4. In change mode, verify data or backend mapping, authorization, reconciliation, recovery, and cutover ownership before dependent work.
5. In change mode, verify affected consumers, entry points, platforms, failures, and data invariants. In planning mode, return stages, acceptance, recovery, and gaps only. For substantive work, use [Quality validation](references/vstack/protocols/quality-validation.md) with the mode, scope, candidate, and evidence; otherwise apply its feedback loop directly. Renew affected verdicts after each repair.
