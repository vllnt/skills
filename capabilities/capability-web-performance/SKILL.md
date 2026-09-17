---
name: capability-web-performance
description: Measure and diagnose web performance, distinguish lab results from field Core Web Vitals, and verify authorized optimizations with comparable before-and-after evidence.
---

# Capability Web Performance

Measure or repair a requested web-performance bottleneck. Discover consumer scripts, browser/Lighthouse versions, budgets, supported devices, and deployment environment; use installed tools without downloading a newer version.

## Procedure

1. Define representative routes, flows, loading/interaction/navigation states, devices, candidate revision, and environment. For lab measurements, record URL, timestamp, tool/version, viewport, CPU/network settings, cache/auth state, and background load. For field data, record source, window, segment, URL/origin coverage, and extraction time.
2. Establish a comparable baseline in the intended environment. Browser execution is required for rendering and interaction metrics; HTTP checks establish transport/server timing, headers, redirects, and payloads only. Do not call total request time TTFB.
3. Separate field from lab evidence. Field Core Web Vitals are 75th-percentile real-visit LCP, INP, and CLS, segmented by device and stated window. Treat published metric thresholds as diagnostic benchmarks; use the consumer's discovered budget for acceptance. Historical field data does not prove the candidate.
4. Treat Lighthouse LCP/CLS/FCP/Speed Index/TBT as tested-session diagnostics. TBT is not INP; a lab interaction is not population INP; absent representative interactions mean INP is unmeasured. Read actual settings rather than assuming desktop throttling behavior.
5. Inspect measured audits, traces, resource timing, bundles, and source to find the bottleneck. Audit savings are estimates. Consult the [optimization playbook](references/optimization-playbook.md) and [page audit snippets](references/eval-audits.md) only when useful.
6. Apply an authorized focused change, preserve functional behavior/accessibility/error handling, then repeat comparable measurements. For noise, report count, median, and spread instead of a selected best run.
7. Report lab gains separately from field results; Lighthouse scores are not certifications. Compare the current evidence with the DoD; repair authorized measured causes and repeat invalidated functional/performance checks. When material risk or uncertainty remains, use independent review and critique perspectives when available, otherwise sequential perspectives. These perspectives assess this procedure; the caller owns overall convergence. Missing browser, field, or authority evidence is incomplete with its next measurement.

Treat traces, HARs, screenshots, and reports as sensitive; sanitize and store raw material only in approved restricted locations. Return baseline/final values with units/provenance, coverage/configuration, cause evidence, changes, regression checks, and limits. A change without a comparable rerun is unverified.

## Definition of Done

- The route, flow, device coverage, candidate, environment, and measurement configuration are recorded.
- Every performance claim has comparable observed baseline and final values with units, provenance, sample count, and variance where needed.
- Lab diagnostics and field Core Web Vitals are distinguished; absent field or representative interaction data remains unmeasured.
- Authorized changes retain functional, accessibility, and error-path evidence; sanitized artifacts preserve the reported proof.
