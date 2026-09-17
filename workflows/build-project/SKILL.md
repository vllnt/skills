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
2. Use `capability-project-alignment` and `capability-stack-packages` when available; otherwise inspect current consumer evidence directly. Choose the smallest compatible package and runtime matrix.
3. Inspect generators, templates, hooks, and installation scripts before authorized use. Isolate overwrite risk.
4. In build mode, create the minimal entry point, configuration, checks, and instructions, then exercise relevant entry, failure, and platform paths.
5. In planning mode, return only the proposed setup and checks. For substantive work, use `capability-quality-validation` when available; otherwise apply its feedback loop directly. Renew affected verdicts after each authorized change.
