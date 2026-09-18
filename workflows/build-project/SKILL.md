---
name: build-project
description: Establish and verify a minimal project baseline from applicable stack and package preferences.
---

## Goal

Establish the smallest authorized project baseline, or return its setup plan. Use `improve-project` to realign an established stack.

### Definition of Done

- Target state, choices, preserved behavior, and platform gaps are explicit.
- A build has a runnable entry point, configuration, instructions, and observed checks.
- A planning result contains setup and checks without edits or execution.
- Current validation accepts the selected mode; an unmet required criterion remains REVISE or BLOCKED.

## Workflow

1. Resolve the target, existing state, required surfaces, rules, permitted effects, preservation criteria, and proof from the request, instructions, and loaded principles.
2. When aligning an existing project or selecting packages, use [Project alignment](references/vstack/capabilities/project-alignment/REFERENCE.md) and [Stack packages](references/vstack/capabilities/stack-packages/REFERENCE.md) with the mode, scope, candidate, and evidence. When the selected stack uses them, use [TypeScript configuration](references/vstack/capabilities/typescript-configuration/REFERENCE.md), [ESLint configuration](references/vstack/capabilities/eslint-configuration/REFERENCE.md), [Workspace Turborepo](references/vstack/capabilities/workspace-turborepo/REFERENCE.md), or [Convex components](references/vstack/capabilities/convex-components/REFERENCE.md); in planning, inspect criteria and propose checks only. Otherwise inspect current consumer evidence directly. Choose the smallest compatible package and runtime matrix.
3. Inspect generators, templates, hooks, and installation scripts before authorized use. Isolate overwrite risk.
4. In build mode, create the minimal entry point, configuration, checks, and instructions, then exercise relevant entry, failure, and platform paths.
5. In planning mode, return only the proposed setup and checks. For substantive work, use [Quality validation](references/vstack/protocols/quality-validation.md) with the mode, scope, candidate, and evidence; otherwise apply its feedback loop directly. Renew affected verdicts after each authorized change.
