---
name: build-prototype
description: Build and iterate a focused local prototype using observed behavior and human product decisions.
---

## Goal

Build one local prototype that tests one product hypothesis, or return its experiment design.

### Definition of Done

- The journey, hypothesis, fidelity, and simulated boundaries are explicit.
- A build has a runnable artifact with observed key, state-change, and error behavior.
- A planning result contains the experiment design and proposed checks only.
- Feedback status, shortcuts, and the recommended next experiment are reported.
- Current validation accepts the selected mode; an unmet required criterion remains REVISE or BLOCKED.

## Boundaries

- Do not present fixture behavior, optional feedback, or simulated integrations as real user acceptance.

## Workflow

1. Resolve the user, problem, journey, hypothesis, constraints, iteration budget, and acceptance criteria from the request, instructions, and loaded principles.
2. Choose visual, fixture-backed, or real-integration fidelity and state what it can prove.
3. In build mode, create the smallest authorized vertical slice and exercise its key, state-change, and error paths.
4. Show the artifact, run instructions, observed behavior, shortcuts, feedback status, and next experiment. In build mode, apply selected feedback when authorized; in planning mode, refine the experiment design only.
5. In planning mode, return the experiment design only. For substantive work, use `capability-quality-validation` when available; otherwise apply its feedback loop directly. Repair authorized gaps and renew affected verdicts until acceptance.
