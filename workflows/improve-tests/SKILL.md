---
name: improve-tests
description: Directly simplify and speed up a test suite while retaining contract coverage, defect detection, and useful diagnostics.
---

## Goal

Change an authorized test suite toward a requested reduction or speed target, choosing its strongest supported improvement one bounded scope at a time. Preserve meaningful protection; a smaller suite is not better if defects become invisible.

### Definition of Done

- The revision, target unit, fixed baseline and discovery scope, relevant contracts, and candidate test scopes are recorded.
- The selected scope has the strongest evidenced maintenance or execution gain relative to effort and risk, and each change is verified before the next.
- Removed tests have retained assertions and representative defect detection or an authorized retired contract; unique failure and diagnostic protection remains.
- Comparable final discovery, skips, coverage scope, detection, and results support the reported change; lasting fixtures and CI wiring match current tests.
- Quality validation accepts the selected mode; achieved reduction, shortfall, and unverified gaps are explicit. An assessment makes no changes or test runs.

## Workflow

1. Resolve mode, authority, consumer rules, contracts, and the requested unit (test cases, test source lines, or measured suite runtime). Freeze baseline revision, scope, denominator, exclusions, discovery configuration, and coverage instrumentation before editing. Do not count newly skipped, undiscovered, or excluded tests as savings. In read-only mode, inspect through step 2, skip steps 3–4, then validate the assessment in step 5 without edits or test runs.
2. Inspect assertions, fixtures, test levels, callers, supported failures, coverage gaps, runtime, and diagnostic value. Use [Code test management](references/vstack/capabilities/code-test-management/REFERENCE.md) with mode and evidence to compare keep, improve, merge, replace, or remove. Rank feasible opportunities by observed cost, overlapping protection, defect risk, effort, and reach; in change mode take a cheap discriminating check when ranking is uncertain; in read-only mode propose it without execution. If the reference is missing, map contracts to actual assertions and distinct failure cases directly; similarity of names or line coverage alone does not establish redundancy.
3. In change mode, select one bounded scope. For preserved contracts, run retained replacements and a representative fault or negative control before deleting scoped cases. For an approved retired contract, verify the change and remaining consumers without inventing replacement coverage. Keep distinct boundary, denial, integration, recovery, and fast diagnostic checks. Diagnose flaky tests rather than silencing them; delete obsolete fixtures only after checking consumers. Retain a recoverable diff and preserve unrelated work.
4. In change mode, rerun affected suites and verify discovery, skip counts, coverage denominators, failure detection, and useful diagnostics against the baseline. Confirm configured CI runs the retained checks and catches a plausible regression, not just that local tests pass. Re-rank after this verified stage and continue only while a supported gain is worth its cost. Update only the owning test contract or fixture documentation needed to keep future maintenance clear.
5. For substantive work, including assessments, use [Quality validation](references/vstack/protocols/quality-validation.md) with mode, current candidate, and evidence; if unavailable, self-assess, obtain independent review and critique where required, triage findings, and renew affected verdicts directly. Rerun invalidated checks after repairs. Report `(baseline - current) / baseline × 100` for a size unit, comparable runtime results for a time unit, the target shortfall, and remaining gaps. Stop rather than weaken detection to hit a percentage; assessment savings are projected, not achieved.
