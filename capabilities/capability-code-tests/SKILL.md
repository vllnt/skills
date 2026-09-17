---
name: capability-code-tests
description: Execute candidate-specific local, development, preview, and CI checks and report verified behavior or remaining gaps.
---

# Capability Code Tests

Establish what an exact candidate demonstrably does. Verification supplies evidence; it never approves, deploys, or publishes.

## Procedure

1. Read consumer instructions and executable configuration. Set candidate identity, consumers, environments, acceptance cases, and permitted effects.
2. Map success, denial, failure, state, and recovery paths. Choose the cheapest checks that exercise real contracts.
3. Run relevant local tests and configured build/type/package checks; record discovery and actual pass/fail/skip counts. A defect fix needs isolated red/green evidence; challenge critical assertions with meaningful negative controls.
4. Exercise the real development interface or built consumer, checking resulting state and forbidden effects. Inspect preview provenance and CI candidate/base/status/artifacts separately; stale, inaccessible, skipped, or unidentified evidence is a gap.
5. When material risk or contradictory evidence remains, use independent review and critique perspectives when available; otherwise apply them sequentially. These perspectives assess this procedure; the caller owns overall convergence. For a repaired candidate or changed input/environment, rerun invalidated local, preview, and CI checks; report the exact next action when setup or access is blocked.

Use [capability-code-test-management](../capability-code-test-management/SKILL.md) only for deeper test design.

## Definition of Done

- The ledger records candidate/service identities, commands, environments, inputs, and actual results.
- Required success, failure, denial, recovery, and consumer evidence is present or explicitly missing.
- Local, preview, and CI evidence stay distinct and candidate-bound.
- The result distinguishes compilation evidence from exercised behavioral evidence.
- A required check that remains missing or failed is reported as incomplete, never as successful verification.
