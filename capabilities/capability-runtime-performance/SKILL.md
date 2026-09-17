---
name: capability-runtime-performance
description: Profile and improve runtime latency, throughput, memory, I/O, query efficiency, scaling, and infrastructure cost against representative workloads and explicit budgets.
---

## Contract

- Input: A target revision, mode, representative workload, environment, budgets, and authority for any runtime changes.
- Output: Baseline and final measurements or a bounded assessment, diagnosed causes, tradeoffs, and unmeasured limits.
- Effects: May make authorized efficiency changes. Production profiling, traffic replay, infrastructure, paid services, database changes, and deployment need separate authority.

### Acceptance

- The target, workload, environment, budgets, and available baseline evidence are recorded.
- Improvement claims have comparable observed baseline and final measurements, samples, variance, and correctness or failure evidence.
- Authorized changes preserve owner interfaces, security, observability, and stated tradeoffs.
- Unrepresentative or unavailable evidence remains a limit, never production proof.

## Procedure

1. Record mode, revision, ownership boundaries, workload distribution and concurrency, environment, resource limits, toolchain, dependencies, and measurement overhead. Use isolated bounded representative data by default.
2. Measure latency percentiles and error rate, throughput, CPU, memory or GC, query plans or count, I/O or network, queues or connections, and cost per successful unit as applicable. Separate user latency from execution or queue time, and measured budgets from proposals or unknowns.
3. Diagnose with profiles, traces, plans, and resource data. Distinguish CPU, memory, contention, dependency latency, saturation, and load-generator effects. Sanitize sensitive evidence.
4. Make the smallest evidence-backed authorized change. Preserve behavior and owner interfaces; address measured computation, allocations, query fan-out, I/O bounds, cancellation, backpressure, retries or deadlines, caches, scaling limits, and observability where applicable.
5. For caches, define ownership, key dimensions, freshness, invalidation, eviction, bounds, and tenant or security isolation; test stale and concurrent behavior. For database changes, evaluate correctness, write or storage cost, and transaction semantics before an authorized migration.
6. Compare baseline and candidate under the same workload, resources, cache, and method. Include appropriate cold or warm, sustained or burst, failure, overload, cancellation, and recovery cases. Report samples and variance, reprofile the current candidate, and run behavior checks.
7. Explain latency, throughput, memory, freshness, reliability, complexity, and cost tradeoffs. Send material uncertainties and comparable proof to the caller's Quality Validation pool. Return the next measurement when representative access, budget, or authority is missing.

## Pitfalls

- Do not trade correctness, reliability, or required security or audit records for speed.
- Runtime measurements do not prove provider savings. Label cost models separately from observed performance.
