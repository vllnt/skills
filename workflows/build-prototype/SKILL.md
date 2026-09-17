---
name: build-prototype
description: Build and iterate a focused local prototype using observed behavior and human product decisions.
---

# Build Prototype

Build one local artifact for one product hypothesis. Planning skips build and execution steps and validates only the experiment design.

## Workflow

1. Confirm user, problem, journey, hypothesis, constraints, iteration budget, and the mode-specific Definition of Done and proof from the request, applicable instructions, and loaded principles; ask only about a product choice that changes the slice.
2. Choose visual, fixture-backed, or real-integration fidelity and state what it can prove.
3. Build the smallest authorized vertical slice with synthetic data where appropriate, then exercise key, state-change, and error paths.
4. Show the artifact, run instructions, observed behavior, shortcuts, feedback status, and the recommended next experiment; never invent feedback or acceptance.
5. Apply selected feedback when available, then validate the artifact or experiment plan against its mode-specific criteria. Use `capability-quality-validation` when available; otherwise self-assess, use independent review and critique for substantive work, or assess perspectives sequentially and state unavailable independence; triage findings, repair only authorized gaps, and renew affected verdicts after a change. Use direct checks for mechanical work. On REVISE, continue authorized repair or plan revision and fresh affected verdicts until acceptance. If a required correction is outside authority, return REVISE with the remedy and required checks. Return BLOCKED only when a required criterion cannot advance, with its next action; missing optional feedback does not block delivery or justify unchanged retries.

## Definition of Done

- Journey, hypothesis, fidelity, and simulated boundaries are explicit.
- Authorized work has a runnable artifact and observed key behavior.
- Planning returns only experiment design and proposed checks.
- Feedback status and remaining shortcuts are reported.
- Completion requires current mode-specific validation acceptance; otherwise report REVISE/BLOCKED with the unmet criterion and next action.
