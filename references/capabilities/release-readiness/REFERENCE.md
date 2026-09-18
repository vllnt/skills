## Contract

- Input: A repository or release candidate, distribution method, public-release requirements, and authorized repair mode.
- Output: A requirement-by-requirement readiness report and any bounded authorized local fixes.
- Effects: Audit is read-only. Repair changes only authorized local artifacts; never publish, alter hosted settings, choose a license, or manage external release state without separate authority.

### Acceptance

- The candidate, distribution method, applicable requirements, and evidence sources are identified.
- Every requirement is pass, gap, unverified, or genuinely not applicable, with evidence and impact.
- Authorized local repairs preserve truthful public content and pass affected checks.
- The report separates release-ready evidence from remaining external validation, publication, or hosting work.

## Procedure

1. Read consumer instructions, candidate revision, distribution method, documentation, manifests, release automation, and applicable checks. Reuse established owners and workflows, including changelog evidence.
2. Classify each applicable requirement as pass, gap, unverified, or not applicable with evidence and impact. Use the [checklist](references/checklist.md); load [CI validation](references/ci-validation.md), [version sync](references/version-sync.md), [LLM catalogs](references/llms-generation.md), or [release messaging](references/release-messaging.md) only when relevant.
3. For authorized repairs, update the owning local artifact with truthful public-safe content. Preserve history and unrelated work; do not invent contacts, compatibility, tests, or project facts.
4. Verify changed artifacts and affected checks. Reclassify changed requirements, repair authorized gaps, and rerun affected checks. Send material unresolved questions and proof to the caller's Quality Validation pool. Return the next check for missing evidence, access, or authority.

## Pitfalls

- Tool or remote-access absence is an evidence gap, not a pass or a reason to stop unaffected assessment.
- Inspect content before exposing it in public documentation or catalogs.
