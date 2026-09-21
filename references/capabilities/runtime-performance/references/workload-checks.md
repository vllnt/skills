# Workload checks

Select cases relevant to the changed path. These scenarios guide verification; they are not measured results or fixed performance budgets.

| Change or failure | Check |
|---|---|
| Query batching removes per-row calls | Compare query count/plans and results on empty, typical, and large data; preserve ordering, pagination, authorization, and transaction semantics. Include batch-size limits. |
| Parallel workers improve average latency | Measure tails, throughput, CPU/memory, downstream connections, and cost under equal load. Burst above capacity: bound queues, apply the documented overload response, then verify recovery. |
| Cache reduces expensive requests | Test cold/warm, invalidation after updates, tenant separation, eviction, simultaneous misses, and bounded memory. Compare results to uncached execution. |
| Streaming reduces memory | Measure peak/retained memory and time to first/last result; simulate slow consumers and cancellation. Confirm no resource leaks or unbounded buffering upstream. |
| Autoscaling proposal lowers idle spend | Measure demand, startup delay, headroom, and downstream limits. Send these inputs to a cost model for billing-unit comparison; treat savings as a projection until an authorized representative run confirms them. |
| New timeout or retry policy | Simulate slow/failed dependencies and partial completion; preserve idempotency and release resources. Show bounded total work rather than amplifying retries during overload. |
| Profiler or production access unavailable | Use bounded local timings, query counts, or instrumented fixtures. Report what they prove and which workload/production claims remain untested. |

Record each run's revision, workload/data seed, environment/resource ceilings, cache state, duration, sample count, error rate, measurements, and cleanup result. Keep baseline and candidate conditions comparable. Preserve sanitized artifacts sufficient to repeat the check; do not commit raw sensitive traces.
