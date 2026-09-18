## Contract

- Input: Consumer rules, contracts, personas, state, callers, test scope, and permitted effects.
- Output: Trustworthy test coverage, observed results, detection evidence, prioritized gaps, and remaining work.
- Effects: Read-only audit or authorized test work. Execution follows consumer rules.

### Acceptance

- Tested contracts, discovery scope, and actual pass/fail/skip results are recorded.
- Changed tests show meaningful detection, not only execution or mock agreement.
- Removed tests have a verified replacement or retired contract.
- Unavailable integration evidence and the next check are explicit.

## Procedure

1. Map contracts, personas, state, callers, and discovery with [coverage](references/coverage.md). Record unknown coverage. In audit mode, return the coverage plan and gaps without creating, pruning, or executing tests.
2. When authorized, run a scoped baseline and distinguish existing failures, skips, missing setup, and new regressions.
3. In authorized test-work mode, prioritize real journeys, boundaries, denials, retries, concurrency, recovery, persistence, and cross-persona handoffs. Prefer real owned collaborators and isolated state.
4. For unavoidable doubles in authorized test work, apply [test-doubles](references/test-doubles.md): document the boundary, verify its contract separately, enforce strict behavior, and retain the integration gap.
5. In authorized test work, verify discovery and sensitivity. Bug tests need isolated red/green evidence; challenge important assertions with a plausible negative control. Before pruning, apply [pruning](references/pruning.md).
6. Return material risks, uncertainties, and current evidence to the caller's quality validation. When standalone, return the prioritized gap and next check. After authorized repairs, rerun invalidated tests and negative controls.

## Pitfalls

- A mocked owned seam is not integration proof; retain the integration gap or use the real collaborator.
- A passing new test does not prove detection; use independently derived expectations or a negative control.
