---
name: capability-project-alignment
description: Assess a new or existing project's fit with applicable stack and package preferences; return a verified target, reusable dependencies, and staged changes without modifying the project.
---

# Capability Project Alignment

Return a target architecture, package selection, and staged changes for the caller to implement. This is read-only: discover preferences from applicable rules and an explicitly selected profile, but do not generate, install, run project code, or migrate.

## Procedure

1. Map requested surfaces, existing behavior, entry points, manifests, lockfiles, runtime versions, integrations, authentication, data owners, and current checks. Mark missing evidence.
2. Resolve the target from applicable instructions. Distinguish existing configuration from the desired state. Choose the smallest reversible option when evidence is sufficient; for a consequential unresolved conflict, state options, recommendation, impact, and the exact decision needed while continuing unaffected analysis.
3. Use `capability-stack-packages` when available for live source, registry, and consumer evidence. Otherwise gather equivalent evidence within the requested scope: selected manifests, paginated source/registry results, exact latest/canary metadata, and consumer declarations/lock resolutions. Report denied access, truncation, source-only packages, and other coverage gaps; keep private evidence out of public artifacts.
4. Match each needed function to an existing preferred package before proposing custom code or another dependency. Verify the exact published version, permitted release channel, exports, peers, engines, supported runtime, maintenance/license fit, and required setup. A source manifest or mutable tag alone does not prove installability or compatibility.
5. Return a decision per candidate: use, keep existing, replace in a named stage, or exclude with evidence. Check cross-surface constraints and extension points; maximize useful reuse, not package count. When registry access is missing, retain a conditional candidate and continue independent work without claiming resolution. Do not reopen a decided option without new material evidence.
6. Define canonical data and authorization owners, client/server boundaries, permitted caches, and external-system interfaces from the target rules. Identify duplicate durable state and business rules. Do not treat client validation or a cache as backend enforcement.
7. Produce small dependency-ordered stages with affected consumers, behavioral acceptance checks, and recovery. Existing data changes need source-to-target mappings, identity/access preservation, validation, cutover ownership, and rollback or roll-forward criteria before execution.
8. For material unresolved target or package decisions, use independent proposal, review, and critique perspectives when available; otherwise cover them sequentially and report the limit. Reconcile evidence and repeat only affected assessment after corrections. Finish only when the DoD holds; missing evidence, access, or authority is incomplete with its next check.

Use the [scenario checks](references/scenarios.md) when evaluating this capability. Selection is read-only evidence; an executing caller must verify installation and actual consumer behavior.

## Definition of Done

- The report identifies the target, applicable rules, existing state, and material unknowns.
- Every proposed package has source/registry, version/channel, peer/runtime, and consumer-resolution evidence or an explicit gap.
- Data, authorization, and integration owners plus dependency-ordered stages have acceptance and recovery checks.
- The assessment returns decisions and evidence only; it does not install, generate, migrate, or change the project.
