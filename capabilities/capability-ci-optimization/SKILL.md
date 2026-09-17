---
name: capability-ci-optimization
description: Audit and optimize CI duration, reliability, runner cost, affected-job selection, and caching while preserving required checks and trust boundaries.
---

# Capability CI Optimization

Inspect or make authorized CI improvements using the repository's provider, workflows, runner setup, toolchain, and required-check policy. Do not assume a provider, monorepo, or billing model.

## Procedure

1. Record mode, revision, event/base/head, workload, runner resources, cache state, job history, and available billing data. Separate measured time/cost from estimates.
2. Map triggers, queue behavior, permissions, secrets, artifacts, dependencies, retries, critical path, merge queues, forks, and provider protection semantics.
3. Change only a measured bottleneck. Without a comparable baseline, return the smallest candidate measurement and decision it can settle. Derive affected work from the full diff, including locks, generated inputs, deletions, and dependents; unknown selection requires conservative validation.
4. Preserve required check identities and fail closed on failed, cancelled, missing, or unexpected skipped work. Cache only trusted, reproducible outputs keyed by relevant source, dependencies, toolchain, platform, and configuration. Protect privileged paths from untrusted forks and cancel only superseded same-change work.
5. Use relevant [scenario checks](references/scenarios.md). Compare equivalent cold and warm runs, including selection, invalidation, failure propagation, fork, cancellation, latency, and cost behavior.
6. For material unresolved questions, use independent review and critique when available; otherwise assess sequentially. Reuse relevant caller evidence while current. After an authorized repair, rerun invalidated scenarios and comparable measurements until required criteria resolve; unavailable runs, billing, or protection evidence yield the exact gap and next check. Do not retry unchanged evidence; return the unresolved criterion and next discriminating check.

## Definition of Done

- Candidate, workload, required checks, and either a measured baseline/bottleneck or the next discriminating measurement are recorded.
- Claimed improvement has comparable measurement and retained protection evidence.
- Cache, selection, cancellation, and failure behavior are checked where changed.
- The result labels unknown evidence as incomplete and bounds the optimization claim to measured evidence.
