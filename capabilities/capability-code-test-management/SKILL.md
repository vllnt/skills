---
name: capability-code-test-management
description: Create, audit, run, improve, and safely prune tests using real behavior and verified defect detection.
---

# Capability Code Test Management

Build the smallest trustworthy suite that detects meaningful broken behavior. A read-only audit does not run project code or mutate state; execution follows consumer rules.

## Procedure

1. Map contracts, personas, state, callers, and discovery with [coverage](references/coverage.md). Record unknown coverage.
2. When authorized, run a scoped baseline and distinguish existing failures, skips, missing setup, and new regressions.
3. Prioritize real journeys, boundaries, denials, retries, concurrency, recovery, persistence, and cross-persona handoffs. Prefer real owned collaborators and isolated state; a mocked owned seam is not integration proof.
4. For unavoidable doubles, apply [test-doubles](references/test-doubles.md): document the boundary, verify its contract separately, enforce strict behavior, and retain the integration gap. Test new behavior with independently derived expectations.
5. Verify discovery and sensitivity. Bug tests must fail before the fix and pass after it in isolation; challenge important assertions with a plausible negative control. Before pruning, apply [pruning](references/pruning.md) and map removed protection to verified retained coverage.
6. When material risk or uncertainty remains, use independent review and critique perspectives when available; otherwise apply them sequentially. These perspectives assess this procedure; the caller owns overall convergence. After each authorized test or code repair, rerun invalidated tests and negative controls until assertions resolve; blocked setup yields a prioritized gap and next check without changing thresholds or expected behavior. Do not retry unchanged evidence; return the unresolved criterion and next discriminating check.

## Definition of Done

- Tested contracts, discovery scope, and actual pass/fail/skip results are recorded.
- Changed tests show meaningful detection, not only execution or mock agreement.
- Removed tests have a verified replacement or retired contract.
- The result identifies unavailable integration evidence and the next check.
