## Contract

- Input: Consumer instructions, executable configuration, candidate, consumers, environments, acceptance cases, and permitted effects.
- Output: Candidate-bound verification ledger, observed behavior, and exact missing or failed checks.
- Effects: Verification only. It never approves, deploys, or publishes.

### Acceptance

- The ledger records candidate/service identities, commands, environments, inputs, and actual results.
- Required success, failure, denial, recovery, and consumer evidence is present or explicitly missing.
- Local, preview, and CI evidence stay distinct and candidate-bound.
- Compilation evidence remains distinct from exercised behavior.
- Missing or failed required checks are incomplete, never successful verification.

## Procedure

1. Read consumer instructions and executable configuration. Set candidate identity, consumers, environments, acceptance cases, and permitted effects.
2. Map success, denial, failure, state, and recovery paths. Choose the cheapest checks that exercise real contracts.
3. Run relevant local tests and configured build/type/package checks; record discovery and actual pass/fail/skip counts. A defect fix needs isolated red/green evidence; challenge critical assertions with meaningful negative controls.
4. Exercise the real development interface or built consumer, checking resulting state and forbidden effects. Inspect preview provenance and CI candidate/base/status/artifacts separately.
5. Return material risks, contradictory evidence, and current proof to the caller's quality validation. When standalone, return the exact blocked check and next action. For repaired candidates or changed input/environment, rerun invalidated checks.

## Pitfalls

- A green preview or CI status does not identify the tested candidate; verify provenance, base, artifacts, and status.
- Compilation supports only the checked build/type properties; exercise a real consumer path before claiming behavioral compatibility.
