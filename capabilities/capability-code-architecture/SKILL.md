---
name: capability-code-architecture
description: Assess architectural friction and recommend smaller modules, clear ownership, traceable dependencies, and behavior-preserving checks.
---

# Capability Code Architecture

Find demonstrated architectural friction and recommend the smallest useful change. This is assessment only: it does not refactor code or authorize implementation.

## Procedure

1. Read consumer rules, source, tests, and decisions. Set candidate revision, scope, intended behavior, constraints, and evidence.
2. Trace entry points, callers, dependency direction, state ownership, and failures. Look for scattered knowledge, pass-through layers, broad interfaces, duplicate ownership, or tests detached from callers.
3. Compare keeping, deleting, consolidating, or extending an existing owner. For each supported option, state callers, preserved behavior, migration risk, and success/failure checks. Prefer no change when benefit is unproven.
4. Return ordered findings with locations, evidence, smallest recommendation, trade-offs, and verification needs. Keep observations, hypotheses, and missing runtime evidence separate.
5. For material ownership, interface, or dependency questions, use independent review and critique perspectives when available; otherwise apply them sequentially. Reuse caller evidence only when candidate, scope, environment, and proof remain current. For a revised candidate, reassess only affected findings and checks until assessment defects resolve; blocked evidence yields coverage gaps and a next check. Do not retry unchanged evidence; return the unresolved criterion and next discriminating check.

Load [LANGUAGE.md](LANGUAGE.md), [DEEPENING.md](DEEPENING.md), or [INTERFACE-DESIGN.md](INTERFACE-DESIGN.md) only when useful.

## Definition of Done

- Scope, callers, ownership/dependency evidence, and coverage limits are explicit.
- Each finding has an observed friction, concrete alternative, and behavior to preserve.
- Recommendations name a verification path and material failure case.
- The conclusion states the assessment boundary and separately labels unverified architecture risks.
