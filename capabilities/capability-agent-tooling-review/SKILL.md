---
name: capability-agent-tooling-review
description: Assess or design a minimal agent-operable control plane with explicit authority, observable outcomes, and safe feedback loops.
---

## Contract

- Input: Consumer rules, candidate, runtime evidence, capability, persona, decision, and authorized action.
- Output: `DESIGN_READY`, `RUNTIME_READY`, `GAPS`, or `BLOCKED`, with evidence, severity, remedy, acceptance check, owner, and missing input.
- Effects: Read-only assessment. It never implements, grants authority, or promotes telemetry into production behavior.

### Acceptance

- Capability, decision, authority boundary, and evidence coverage are identified.
- Findings trace to an observed control gap or a concrete design requirement.
- `DESIGN_READY` has a specified implementation contract; `RUNTIME_READY` has observed real-path proof.
- Unobserved paths and the next check remain explicit.

## Procedure

1. Read consumer rules, contracts, tests, and runtime evidence. Set the candidate and required success evidence.
2. Trace `observe → diagnose → preflight → act → receipt → reobserve → learn`. Check typed outcomes, correlation IDs, reasons, cancellation/recovery, human/agent parity, and a path outside a human-only dashboard.
3. Check that actions have explicit authority and receipts; failures have an owner and next safe action; feedback has provenance and a promotion gate. Omit signals with no decision-making consumer; do not retain secrets, raw prompts, or hidden reasoning.
4. Return material uncertainties and current evidence to the caller's quality validation. When standalone, assess sequentially and return the unresolved criterion and next check. Reassess only paths affected by changed evidence.
5. Return the readiness state. If evidence, authority, or access is blocked, return the gap and next discriminating check.

## Pitfalls

- Telemetry proves a runtime path only when the event has provenance and the current candidate/environment are identified; otherwise report it as unverified.
- A dashboard-only action path does not prove agent operability; trace an agent-accessible path.
