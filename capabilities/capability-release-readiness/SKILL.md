---
name: capability-release-readiness
description: Assess public-release readiness and repair authorized local documentation, metadata, and workflow gaps.
---

# Capability Release Readiness

Assess a repository or release candidate against its own public-release requirements. Audit is read-only; an explicit repair request authorizes only bounded local fixes. This skill does not publish, alter hosted settings, choose a license, or manage external release state without separate authority.

## Procedure

1. Read consumer instructions, candidate revision, distribution method, existing documentation, manifests, release automation, and applicable checks. Reuse established owners and workflows. Treat existing changelog maintenance as its own owner; consume its evidence rather than rewriting its process.
2. Classify each applicable requirement as pass, gap, unverified, or not applicable, with evidence and impact. Use the [checklist](references/checklist.md); load [CI validation](references/ci-validation.md), [version sync](references/version-sync.md), [LLM catalogs](references/llms-generation.md), or [release messaging](references/release-messaging.md) only when relevant.
3. For authorized repairs, update the owning local artifact with truthful, public-safe content. Keep optional documents consumer-defined, preserve history and unrelated work, and do not invent contacts, compatibility, tests, or project facts.
4. Verify changed artifacts and affected checks. Compare the current candidate with the DoD; repair authorized local gaps and repeat affected checks with independent review/critique for material unresolved questions when available, otherwise sequential perspectives. Reclassify changed requirements; missing evidence, access, or authority is incomplete with its next check.

Inspect content before exposing it in public documentation or catalogs. Apply reversible fixes within the approved scope without repeated per-write confirmation; ask only for consequential missing authority or decisions. Tool or remote-access absence is an evidence gap, not a reason to stop the assessment.

## Definition of Done

- The candidate, distribution method, applicable requirements, and evidence sources are identified.
- Every requirement is pass, gap, unverified, or genuinely not applicable, with evidence and impact.
- Authorized local repairs preserve truthful public content and pass affected artifact and repository checks.
- The report separates release-ready evidence from remaining external validation, publication, or hosting work.
