---
name: improve-codebase
description: Directly refactor source code and client/server data paths toward measured reduction and efficiency while preserving behavior.
---

## Goal

Make and verify authorized code and data-path changes, prioritizing the strongest supported gain one bounded scope at a time. Preserve supported features and leave clear owners, contracts, tests, and diagnostics. A percentage is a target, not a deletion quota.

### Definition of Done

- The revision, requested target, source unit, fixed baseline and exclusions, supported contracts, callers, and candidate scopes are recorded.
- The selected scope has the strongest evidenced gain relative to effort and risk; each authorized change and its verification finish before selecting another.
- Affected consumers preserve success, failure, security, freshness, and recovery behavior; tests retain meaningful detection.
- Claimed code or data-path gains have comparable before/after evidence, without moving cost or code out of the measured scope; lasting contracts and diagnostics reflect the result.
- Quality validation accepts the selected mode; achieved gain, shortfall, tradeoffs, and unverified requirements are explicit. An assessment makes no changes or test runs.

## Boundaries

- Production profiling, traffic replay, migrations, deployments, and external-service changes need their own authority. Use bounded isolated evidence within scope and report missing proof or approval instead of silently changing those systems.

## Workflow

1. Resolve mode, authority, consumer rules, requested source-reduction or efficiency goals, and applicable constraints. For a broad request spanning source, tests, and developer workflows, compare supported gains across owners first; route the strongest test-only or DX scope to `improve-tests` or `improve-dx` in the same mode when available, then re-rank after its verification; otherwise report the routing gap and work on the next supported scope without claiming the overall greatest gain. Fix the baseline revision, unit (for example, tracked maintained source lines), scope, denominator, and exclusions before editing. Exclude generated and vendored files consistently; do not count moved code or outsourced work as savings. If no number is supplied, improve demonstrated maintenance cost without inventing X. In read-only mode, inspect through step 2, skip steps 3–5, then validate the assessment in step 6 without edits or test runs.
2. Trace affected callers, owners, state, and journeys through client → API → server → storage where applicable. Map supported outputs, failures, authorization, freshness, retries, and existing tests. In change mode, run authorized baseline checks and representative workloads. Use [Code architecture](references/vstack/capabilities/code-architecture/REFERENCE.md) to compare ownership and [Runtime performance](references/vstack/capabilities/runtime-performance/REFERENCE.md) for performance claims, passing mode and evidence. Rank feasible code/data opportunities by observed impact, repeatability, effort, and risk; if uncertain, take the cheapest discriminating measurement in change mode or propose it in read-only mode. Without a reference, inspect owners/callers directly and claim speed only from comparable isolated measurements. Do not infer a bottleneck from source shape alone.
3. In change mode, choose one bounded scope and implement its smallest useful fix: remove verified duplication or dead paths, consolidate scattered responsibility at the existing owner, or reduce measured fetching, transformations, serialization, or round trips. Preserve public interfaces, dependency direction, validation, tenant isolation, cancellation, and failure semantics. For a cache or tier move, check total cost, key dimensions, freshness, invalidation, and cross-tenant behavior. Do not compress code or hide work to meet a target.
4. Use [Code test management](references/vstack/capabilities/code-test-management/REFERENCE.md) for affected tests in change mode. Keep unique boundary, denial, and integration protection. Before removing a test for preserved behavior, map its contract to retained assertions, run the replacement and representative defect challenge, then recheck discovery, skips, and coverage scope. For an approved retired contract, verify the retirement and remaining consumers instead of inventing replacement coverage. If the reference is missing, apply the same gates directly; without proof, keep the test. Test-suite-only reductions belong to `improve-tests` when installed, but this workflow still verifies its own changed and dependent consumers.
5. In change mode, exercise relevant success, failure, denial, retry, concurrency, persistence, and recovery paths through real affected callers. Compare performance under equivalent workloads and resources; report latency, error, payload, request, and resource tradeoffs as applicable. Update owning contracts, focused regression checks, and diagnostics; when retiring a path, verify configured test/CI discovery exercises its replacement. Re-rank after observed results and continue only while another authorized gain is worth its cost, one scope at a time.
6. For substantive work, including assessments, use [Quality validation](references/vstack/protocols/quality-validation.md) with mode, current candidate, and evidence; if unavailable, self-assess, obtain independent review and critique where required, triage findings, and renew affected verdicts directly. Rerun invalidated checks after repairs. Report achieved source reduction as `(baseline - current) / baseline × 100`, measured efficiency changes, unmet targets, and gaps. Stop short of goals that require weaker behavior or detection; assessment savings are projected, not achieved.
