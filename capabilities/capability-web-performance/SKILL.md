---
name: capability-web-performance
description: Measure and diagnose web performance, distinguish lab results from field Core Web Vitals, and verify authorized optimizations with comparable before-and-after evidence.
---

## Contract

- Input: A web-performance target, routes or flows, candidate revision, supported devices, environment, budgets, and authorized change scope.
- Output: Comparable lab or field evidence, diagnosed causes, authorized optimizations or findings, and measurement limits.
- Effects: May apply authorized focused changes. Do not download newer tools automatically.

### Acceptance

- The route, flow, device coverage, candidate, environment, and measurement configuration are recorded.
- Each performance claim has comparable observed baseline and final values with units, provenance, sample count, and variance when needed.
- Lab diagnostics and field Core Web Vitals are distinguished; absent field or representative interaction data remains unmeasured.
- Authorized changes retain functional, accessibility, and error-path evidence; sanitized artifacts preserve proof.

## Procedure

1. Discover consumer scripts, installed browser or Lighthouse versions, budgets, devices, and deployment environment. Define routes, flows, states, candidate, and environment. Record lab URL, time, tool or version, viewport, CPU or network settings, cache or auth state, and background load; record field source, window, segment, coverage, and extraction time.
2. Establish a comparable baseline in the intended environment. Browser execution is required for rendering and interaction metrics; HTTP checks establish transport or server timing, headers, redirects, and payloads only.
3. Separate field from lab evidence. Field Core Web Vitals are 75th-percentile real-visit LCP, INP, and CLS, segmented by device and stated window. Use the consumer's discovered budget for acceptance; treat published thresholds as diagnostic benchmarks.
4. Treat Lighthouse LCP, CLS, FCP, Speed Index, and TBT as tested-session diagnostics. Inspect audits, traces, resource timing, bundles, and source to identify the bottleneck; audit savings are estimates. Load the [optimization playbook](references/optimization-playbook.md) or [page audit snippets](references/eval-audits.md) only when useful.
5. Apply an authorized focused change, preserve functional behavior, accessibility, and error handling, then repeat comparable measurements. For noise, report count, median, and spread rather than a selected best run.
6. Report lab gains separately from field results, including baseline and final values, units, provenance, configuration, cause evidence, changes, regression checks, and limits. Send material uncertainty and proof to the caller's Quality Validation pool. Return the next measurement for missing browser, field, or authority evidence.

## Pitfalls

- Total request time is not TTFB. Inspect the metric definition and measurement source.
- TBT is not INP, a lab interaction is not population INP, and historical field data does not prove the current candidate.
