---
name: capability-runtime-performance
description: Profile and improve runtime latency, throughput, memory, I/O, query efficiency, scaling, and infrastructure cost against representative workloads and explicit budgets.
---

# Capability Runtime Performance

Inspect, validate, or make authorized runtime efficiency improvements for services, applications, batch jobs, and libraries. Use repository-native profilers and workloads; production profiling, traffic replay, infrastructure changes, paid services, database changes, and deployment need separate authority.

## Procedure

1. Record mode, revision, ownership boundaries, workload (data distribution, concurrency, arrival/read-write mix, cache, steady/burst), environment, resource limits, toolchain, dependencies, and measurement overhead. Use isolated, bounded representative data by default.
2. Measure the relevant baseline: latency percentiles/error rate, throughput, CPU, memory/GC, query plans/count, I/O/network, queues/connections, and cost per successful unit. Separate user latency from execution/queue time and measured budgets from proposals or unknowns. Provide measured demand and unit-cost inputs to a cost model when financial comparison is requested.
3. Diagnose with profiles, traces, plans, and resource data; distinguish CPU, memory, contention, dependency latency, saturation, and load-generator effects. Sanitize sensitive evidence.
4. Make the smallest evidence-backed change. Preserve behavior and owner interfaces; address measured computation, allocations, query fan-out/scans/overfetch, I/O bounds, cancellation, backpressure, retry/deadline policy, caches, scaling limits, and required observability as applicable.
5. For caches, define ownership, key dimensions, freshness, invalidation, eviction, bounds, and tenant/security isolation; test stale and concurrent behavior. For database changes, evaluate correctness, write/storage cost, and transaction semantics before any authorized migration.
6. Do not trade correctness, reliability, or required audit/security records for a faster result. Explain latency, throughput, memory, freshness, reliability, complexity, and cost tradeoffs; label modeled cost separately and do not claim provider savings from runtime measurements alone.
7. Follow relevant [workload checks](references/workload-checks.md): reproduce the old regression in isolation, compare candidate/baseline under the same workload/resource/cache/method, include appropriate cold/warm, sustained/burst, failure, overload, cancellation, and recovery cases, and bound duration/resources with cleanup.
8. Report samples and variance, reprofile the current candidate, and run behavior checks. Compare it with the DoD; repair authorized measured causes and repeat invalidated workload checks with independent review/critique for material unresolved questions when available, otherwise sequential perspectives. Missing representative access, budget, or authority is incomplete with its next measurement.

Use installed equivalents, local instrumentation, bounded fixtures, or code/query analysis when a representative environment is unavailable. Return useful evidence and explicit limits rather than an unmeasured improvement.

## Definition of Done

- The target, workload, environment, budgets, and available baseline evidence are recorded; an assessment may report an unavailable baseline as a limit.
- Any performance improvement claim has comparable observed baseline and final measurements, samples, variance, and unchanged correctness/failure evidence.
- Authorized changes preserve owner interfaces, security, observability, and stated tradeoffs.
- Unrepresentative or unavailable runtime evidence is reported as a limit, never production proof.
