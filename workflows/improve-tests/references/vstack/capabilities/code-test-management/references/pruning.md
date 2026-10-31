# Safe test improvement and pruning

## Decide what a test protects

Read assertions, fixtures, setup, history when useful, and the current public contract. Similar names, touched lines, or snapshots do not establish redundancy. Record unique inputs, denied actions, boundary values, failure modes, supported environments, and diagnostic value.

Choose one:

- **Keep:** unique meaningful protection or useful fast localization.
- **Improve:** weak oracle, flaky setup, excessive mocking, implementation coupling, stale fixture, or unawaited work.
- **Merge/replace:** retained tests cover the same required behaviors and representative defects with lower maintenance cost.
- **Remove:** behavior is explicitly retired, test cannot exercise any meaningful contract, or a verified replacement preserves its protection.

## Removal gate

1. Name the removed test's contract and why removal is justified.
2. Map required cases to specific retained assertions; do not assume a happy-path E2E replaces unit boundary cases.
3. Run replacements first. Challenge representative defects to verify they still fail for the intended reason. For retired behavior, cite the approved contract change rather than making up replacement coverage.
4. Preserve a recoverable diff or patch before deletion, especially for untracked tests. Do not overwrite unrelated changes.
5. Remove only the approved scoped cases; rerun relevant suites and verify test discovery, skip counts, and coverage denominators. Fewer executed tests or excluded files are not an improvement by themselves.
6. Report removals, mappings, changed runtime if measured, and remaining risks.

## Common traps

- A failing test may reveal a product bug, not an obsolete requirement.
- A flaky test is a reliability defect. Diagnose shared state, readiness, timing, leaked resources, and order dependence; repeat the relevant conditions, not retries-until-green.
- Quarantine requires explicit authorization, a stated coverage gap, and a tracked repair/expiry condition. It is not a passing result.
- Review snapshot changes semantically. Keep snapshots where the whole output is a real contract; replace broad incidental snapshots with focused assertions otherwise.
- Avoid call-count assertions unless invocation itself is the contract, such as exactly-once submission. Verify the real resulting effect too where feasible.
- Removing every narrow unit test in favor of slow journeys can reduce fault detection and increase diagnosis cost. Optimize protection and maintainability, not test count alone.
