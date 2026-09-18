## Contract

- Input: A project scope, existing evidence, applicable rules, and an explicitly selected stack profile.
- Output: A read-only target architecture, package decisions, ownership boundaries, staged changes, and evidence gaps.
- Effects: Read-only assessment. Do not generate, install, run project code, or migrate.

### Acceptance

- The target, applicable rules, existing state, and material unknowns are explicit.
- Each proposed package has source, registry, version or channel, peer or runtime, and consumer-resolution evidence, or an explicit gap.
- Data, authorization, and integration owners have dependency-ordered stages with acceptance and recovery checks.
- The report contains decisions and evidence only.

## Procedure

1. Map requested surfaces, existing behavior, entry points, manifests, lockfiles, runtime versions, integrations, authentication, data owners, and current checks. Mark missing evidence.
2. Resolve the target from applicable instructions. Distinguish existing configuration from the desired state. Select the smallest reversible option supported by evidence; for consequential conflict, state options, recommendation, impact, and the required decision while continuing unaffected analysis.
3. Use [Stack packages](../stack-packages/REFERENCE.md) for current source, registry, and consumer evidence when available. Otherwise gather equivalent scoped evidence: selected manifests, paginated source or registry results, exact latest or canary metadata, and consumer declarations or lock resolutions.
4. Match each needed function to a preferred existing package before proposing custom code or another dependency. Verify exact published version, permitted channel, exports, peers, engines, runtime, maintenance or license fit, and required setup.
5. Return a decision for each candidate: use, keep, replace in a named stage, or exclude with evidence. Check cross-surface constraints and extension points; maximize useful reuse rather than package count.
6. Define canonical data and authorization owners, client or server boundaries, permitted caches, and external interfaces from target rules. Identify duplicate durable state and business rules.
7. Produce small dependency-ordered stages with consumers, behavioral acceptance checks, and recovery. For existing data changes, include mapping, identity or access preservation, validation, cutover ownership, and rollback or roll-forward criteria.
8. Return the assessment and its next check for every unresolved gap. Send material decisions, uncertainties, and evidence to the caller's Quality Validation pool.

## Pitfalls

- A source manifest or mutable tag does not prove installability or compatibility. Verify the selected release and consumer resolution.
- Client validation or a cache does not establish backend enforcement. Identify the canonical enforcement owner.
