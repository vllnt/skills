## Contract

- Input: Candidate, event/base/head, workflow configuration, runner/cache state, job history, and available billing data.
- Output: Measured bottleneck or next discriminating measurement, improvement evidence, retained protection evidence, and remaining gaps.
- Effects: Read-only audit or authorized CI changes. It preserves required check identities and provider trust boundaries.

### Acceptance

- Candidate, workload, required checks, and a measured baseline/bottleneck or next measurement are recorded.
- Claimed improvement has comparable measurement and retained protection evidence.
- Changed cache, selection, cancellation, and failure behavior are checked.
- Unknown runs, billing, or protection evidence remains incomplete.

## Procedure

1. Record mode, candidate, workload, runner resources, cache state, history, and billing data. Separate measured time/cost from estimates.
2. Map triggers, queues, permissions, secrets, artifacts, dependencies, retries, critical path, merge queues, forks, and protection semantics.
3. In audit mode, propose the measured bottleneck, smallest change, and validating check. In authorized change mode, apply only a measured fix. Derive affected work from the full diff, including locks, generated inputs, deletions, and dependents. Use conservative validation when selection is unknown.
4. Preserve required checks; cancel only superseded runs for the same change. Fail closed on failed, cancelled, missing, or unexpected skipped work; cache only trusted reproducible outputs; protect privileged paths from untrusted forks.
5. Run relevant [scenario checks](references/scenarios.md). Compare equivalent cold and warm runs, including invalidation, failure propagation, forks, cancellation, latency, and cost.
6. Return material uncertainties and current evidence to the caller's quality validation. When standalone, return the unresolved criterion and next discriminating check. After an authorized repair, rerun invalidated scenarios and comparable measurements.

## Pitfalls

- A faster run without an equivalent workload or retained required checks is not an optimization claim; compare like-for-like runs.
- A cache hit does not establish safe invalidation; exercise a changed dependency, toolchain, platform, or configuration.
