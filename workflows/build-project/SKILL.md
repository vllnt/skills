---
name: build-project
description: Establish and verify a minimal project baseline from applicable stack and package preferences.
---

# Build Project

Create a new baseline or add a missing one; use `improve-project` for established-stack realignment. Planning only inspects and proposes.

## Workflow

1. Confirm target, required surfaces, existing state, rules, effects, and behavior to preserve.
2. Use `capability-project-alignment` when available for target decisions and its `capability-stack-packages` composition for current evidence; otherwise perform those checks directly. Resolve the smallest compatible package and runtime matrix from consumer rules and available evidence; ask only about consequential choices.
3. Inspect generators, templates, hooks, and install scripts before authorized use; isolate any overwrite risk.
4. Build the minimal entry point, configuration, checks, and instructions, then exercise relevant entry, failure, and platform paths. A web build does not prove native behavior.
5. Use distinct review or critique perspectives when they add evidence proportional to the change; otherwise assess sequentially. Repair permitted gaps and rerun affected checks. If blocked, state the cause, viable options, recommendation, consequence, and next action; report only the observed partial baseline as verified.

## Definition of Done

- Target state, choices, and preserved behavior are recorded.
- An authorized build has runnable entry, configuration, instructions, and observed checks.
- Planning returns setup and checks without edits or execution.
- Platform gaps are explicit.
