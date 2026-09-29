---
name: improve-dx
description: Directly reduce measured build, lint, script, and CI friction without hiding failures or skipping required checks.
---

## Goal

Improve developer workflows in authorized change mode by selecting the highest-supported gain and changing one bounded scope at a time. Preserve outputs, diagnostics, required checks, and trusted execution; a faster green run must still detect real failures.

### Definition of Done

- The revision, affected tasks, required checks, representative workloads, baseline timings and outputs, and requested targets are recorded.
- The selected scope has the strongest evidenced gain relative to effort and risk; each authorized change and verification finish before the next.
- Changed builds, lint rules, scripts, or CI still produce supported artifacts and diagnostics, propagate failures, and respect cache and permission boundaries.
- Comparable final cold/warm or CI critical-path evidence supports claimed gains; lasting scripts, configuration, and checks reflect the result.
- Quality validation accepts the selected mode; achieved gain, tradeoffs, shortfall, and unverified gaps are explicit. An assessment makes no changes or test runs.

## Boundaries

- Remote workflow changes, paid infrastructure, privileged secrets, and deployments follow consumer authority. Measure locally or with authorized hosted evidence; missing provider proof stays unverified.

## Workflow

1. Resolve mode, scope, consumer rules, authority, requested time or maintenance target, and required validation. Fix revision, runner/toolchain, workload, resources, cache state, units, and exclusions before changing tasks. Separate queue from execution time, and cold from warm build/lint or CI runs. In read-only mode, inspect through step 2, skip steps 3–4, then validate the assessment in step 5 without edits or test runs.
2. Trace scripts, task prerequisites, produced artifacts, consumers, lint file/rule scope, CI triggers, critical path, selection, permissions, and caches. Sample available comparable runs and rank opportunities by repeatable wall-time or maintenance gain relative to effort and failure risk; if uncertain, take the cheapest discriminating measurement in change mode or propose it in read-only mode. Use [CI optimization](references/vstack/capabilities/ci-optimization/REFERENCE.md) for CI changes, [Workspace Turborepo](references/vstack/capabilities/workspace-turborepo/REFERENCE.md) only when its runner applies, and [ESLint configuration](references/vstack/capabilities/eslint-configuration/REFERENCE.md) only for ESLint config changes, passing mode and evidence. Without these references or runners, inspect native scripts/configuration and required checks directly; do not infer speed or safety from a green run alone.
3. In change mode, choose one bounded scope and apply the smallest measured fix: remove a verified redundant script, repair task ordering, narrow repeated work without losing affected dependents, or improve trusted cache inputs and outputs. Preserve script interfaces, build artifacts, lint diagnostics and file scope, required CI check identities, and fail-closed behavior on failed, missing, cancelled, or unexpected skipped work. If affected work is unknown after a deletion, missing base, or task-graph gap, choose conservative full relevant validation rather than skip possible dependents. Do not mask slow work by excluding files, tests, or dependent tasks, or let untrusted code poison privileged caches.
4. In change mode, compare equivalent cold/warm outputs and timings, including changed source, locks, configuration, and environment inputs as relevant. Exercise a deliberately failing lint/build/test case and CI-equivalent selection and failure propagation; verify consumers of artifacts and scripts. Record samples and variability, cache invalidation, queue and critical-path effects separately. Re-rank after the verified stage and continue only while another supported gain is worth its cost, one scope at a time. Update owning task configuration and necessary documentation; avoid a new standing process without need.
5. For substantive work, including assessments, use [Quality validation](references/vstack/protocols/quality-validation.md) with mode, candidate, and evidence; if unavailable, self-assess, obtain independent review and critique where required, triage findings, and renew affected verdicts directly. Rerun invalidated checks after repairs. Report comparable time and output changes, any measured script-size reduction in its fixed unit, targets missed, and remaining gaps. Stop short of any target that requires weaker required checks or diagnostics; assessment gains are projected, not achieved.
