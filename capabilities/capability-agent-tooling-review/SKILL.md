---
name: capability-agent-tooling-review
description: Assess or design a minimal agent-operable control plane with explicit authority, observable outcomes, and safe feedback loops.
---

# Capability Agent Tooling Review

Assess an agent-operated capability or design its smallest control-plane contract. This is read-only: it never implements, grants authority, or promotes telemetry into production behavior.

## Procedure

1. Read consumer rules, contracts, tests, and runtime evidence. Set the capability, persona, decision, authorized action, candidate, and success evidence.
2. Trace `observe → diagnose → preflight → act → receipt → reobserve → learn`. Check typed outcomes, correlation IDs, reasons, cancellation/recovery, human/agent parity, and a path outside a human-only dashboard.
3. Check that actions have explicit authority and receipts; failures have an owner and next safe action; feedback has provenance and a promotion gate. Omit signals with no decision-making consumer and retain no secrets, raw prompts, or hidden reasoning.
4. Return `DESIGN_READY`, `RUNTIME_READY`, `GAPS`, or `BLOCKED` with evidence, severity, smallest remedy, acceptance check, decision owner, and missing input. `DESIGN_READY` means the implementation contract is specified; `RUNTIME_READY` requires observed real-path proof.
5. For material unresolved questions, use independent review and critique when available; otherwise assess sequentially. Reuse relevant caller evidence while current. On candidate or evidence changes, reassess affected paths and checks; blocked access, authority, or evidence yields an incomplete result and next check without retrying unchanged evidence.

## Definition of Done

- Capability, decision, authority boundary, and evidence coverage are identified.
- Findings trace to an observed control gap or a concrete design requirement.
- The selected readiness level is explicit: design requirements are resolved for DESIGN_READY; runtime claims have real-path proof for RUNTIME_READY. Unobserved paths and the next check remain named.
