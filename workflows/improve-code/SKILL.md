---
name: improve-code
description: Simplify code and comments and refactor source and data paths for measured reduction and efficiency while preserving observable contracts and affected consumers.
---

## Goal

Reduce demonstrated maintenance cost and, when asked, measured source size or data-path cost while preserving supported behavior: simplify code and comments or refactor source and data paths, strongest gain first, one bounded scope at a time. A percentage is a target, not a deletion quota.

### Definition of Done

- Mode, target, fixed baseline (revision, unit, denominator, exclusions), contracts, callers, and candidate scopes are recorded.
- The strongest evidenced gain relative to effort and risk is selected and verified before the next; assessment returns ranked candidates and checks without changes or test runs.
- Consumers keep success, failure, security, freshness, and recovery behavior; tests retain meaningful detection.
- Claimed gains have comparable before/after evidence without moving cost or code out of the measured scope; contracts, regression checks, and diagnostics reflect the result.
- Quality validation accepts the mode; gain, shortfall, tradeoffs, and unverified requirements are explicit.

## Boundaries

- Production profiling, traffic replay, migrations, deployments, and external-service changes need their own authority; use bounded isolated evidence and report missing proof or approval.

## Workflow

1. Resolve mode, authority, consumer rules, goals, and constraints; discover languages, entry points, and native commands without imposing a framework. For a broad request spanning source, tests, and developer workflows, route the strongest test-only or DX scope to `improve-tests` or `improve-dx` in the same mode when available, then re-rank; otherwise report the gap and take the next supported scope without claiming the overall greatest gain. Fix the baseline before editing, excluding generated and vendored files consistently; with no number, reduce demonstrated maintenance cost without inventing one. Steps 3–4 are change mode only; read-only mode makes no edits or test runs.
2. Trace real callers, owners, state, and data paths without assuming a web tier or database, and check test, build, deployment, and recovery consumers before declaring code unused. Map outputs, failures, authorization, freshness, retries, and tests; in change mode run baseline checks and workloads. Use [Code architecture](references/vstack/capabilities/code-architecture/REFERENCE.md) for ownership, [Code test management](references/vstack/capabilities/code-test-management/REFERENCE.md) for tests in scope, [Runtime performance](references/vstack/capabilities/runtime-performance/REFERENCE.md) for speed claims, and [Workspace Turborepo](references/vstack/capabilities/workspace-turborepo/REFERENCE.md) only for a Turborepo workspace boundary in scope. Rank by impact, repeatability, effort, and risk, dropping cosmetic churn and merging overlapping work; if uncertain, measure cheaply (change mode) or propose it (read-only). Claim speed only from comparable isolated measurements, not source shape.
3. Make the smallest fix for one bounded scope, preferring deletion or existing interfaces: remove verified duplication or dead paths, consolidate responsibility at its owner, or cut measured fetching, transformation, serialization, or round trips. Preserve public interfaces, dependency direction, validation, errors, documentation, tenant isolation, cancellation, and failure semantics. Apply the [change checks](references/change-checks.md) to cache or tier moves, test removal, and path retirement. Never compress code or hide work to hit a target.
4. Exercise real affected callers before and after across applicable success, failure, denial, retry, concurrency, persistence, recovery, compatibility, packaging, and build paths, and compare performance under equivalent workloads, reporting tradeoffs. Re-rank; continue only while another authorized gain is worth its cost.
5. For substantive work, including assessments, use [Quality validation](references/vstack/protocols/quality-validation.md), with [Code review](references/vstack/capabilities/code-review/REFERENCE.md) in review mode for medium and high tiers; rerun invalidated checks. Report `(baseline - current) / baseline × 100`, efficiency changes, unmet targets, and gaps. Stop short of goals needing weaker behavior or detection; assessment savings are projected, not achieved.
