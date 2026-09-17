---
name: capability-code-architecture
description: Assess architectural friction and recommend smaller modules, clear ownership, traceable dependencies, and behavior-preserving checks.
---

## Contract

- Input: Consumer rules, candidate revision, source, tests, decisions, scope, intended behavior, and constraints.
- Output: Ordered evidence-backed findings, smallest alternatives, trade-offs, verification needs, and coverage gaps.
- Effects: Read-only assessment. It does not refactor code or authorize implementation.

### Acceptance

- Scope, callers, ownership/dependency evidence, and coverage limits are explicit.
- Each finding has observed friction, a concrete alternative, and behavior to preserve.
- Recommendations name a verification path and material failure case.
- Unverified architecture risks remain separate from conclusions.

## Procedure

1. Read consumer rules, source, tests, and decisions. Set the candidate, scope, intended behavior, constraints, and evidence.
2. Trace entry points, callers, dependency direction, state ownership, and failures. Look for scattered knowledge, pass-through layers, broad interfaces, duplicate ownership, and tests detached from callers.
3. Compare keeping, deleting, consolidating, or extending an existing owner. State callers, preserved behavior, migration risk, and success/failure checks. Prefer no change when benefit is unproven.
4. Return findings with locations, evidence, smallest recommendation, trade-offs, and verification needs. Keep observations, hypotheses, and missing runtime evidence separate.
5. Return material ownership, interface, or dependency uncertainties and current evidence to the caller's quality validation. When standalone, return the coverage gap and next check. Reassess only affected findings when evidence changes.

Load [LANGUAGE.md](LANGUAGE.md), [DEEPENING.md](DEEPENING.md), or [INTERFACE-DESIGN.md](INTERFACE-DESIGN.md) only when useful.

## Pitfalls

- Source structure alone does not prove runtime friction; label runtime behavior unverified until it is observed.
- A smaller module is not automatically a better boundary; compare preserved callers and ownership before recommending a split.
