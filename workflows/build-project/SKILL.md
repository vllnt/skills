---
name: build-project
description: Establish and verify a minimal project baseline from applicable stack and package preferences.
---

# Build Project

Create a new baseline or add a missing one; use `improve-project` for established-stack realignment. Planning skips build and execution steps and validates only the proposed plan.

## Workflow

1. Confirm target, required surfaces, existing state, rules, effects, preserved behavior, and the mode-specific Definition of Done and proof from the request, applicable instructions, and loaded principles.
2. Use `capability-project-alignment` when available for target decisions and its `capability-stack-packages` composition for current evidence; otherwise perform those checks directly. Resolve the smallest compatible package and runtime matrix from consumer rules and available evidence; ask only about consequential choices.
3. Inspect generators, templates, hooks, and install scripts before authorized use; isolate any overwrite risk.
4. Build the minimal entry point, configuration, checks, and instructions, then exercise relevant entry, failure, and platform paths. A web build does not prove native behavior.
5. Validate the baseline or plan against its mode-specific criteria. Use `capability-quality-validation` when available; otherwise self-assess, use independent review and critique for substantive work, or assess perspectives sequentially and state unavailable independence; triage findings, repair only authorized baseline gaps, and renew affected verdicts after a change. Use direct checks for mechanical work. On REVISE, continue authorized repair or plan revision and fresh affected verdicts until acceptance. If a required correction is outside authority, return REVISE with the remedy and required checks. Return BLOCKED only when a required criterion cannot advance, with its next action; do not retry unchanged evidence.

## Definition of Done

- Target state, choices, and preserved behavior are recorded.
- An authorized build has runnable entry, configuration, instructions, and observed checks.
- Planning returns setup and checks without edits or execution.
- Platform gaps are explicit.
- Completion requires current mode-specific validation acceptance; otherwise report REVISE/BLOCKED with the unmet criterion and next action.
