---
name: capability-release-changelog
description: Maintain accurate user-facing change history and local release notes without publishing a release.
---

# Capability Release Changelog

Use this skill to add, report, prepare, backfill, or repair change history. It owns the existing changelog and pending-entry files. It does not own version manifests, tags, hosted releases, or publishing.

## Procedure

1. Read the consumer repository's instructions, current history, release process, and evidence for the requested change. Set the history owner and requested operation. Reuse its direct `[Unreleased]` section, fragments, or generator. Use [format examples](references/format.md) only when no format is established.
2. Choose the requested operation. Report is read-only. Add writes one concise pending outcome. Prepare release promotes only the approved entries into the approved version and date. Backfill adds only evidenced omissions. Repair corrects authorized structural drift without rewriting released meaning.
3. Use public-safe, evidence-backed wording. A commit subject is a lead, not proof of behavior; mark uncertain shipment, version, date, or link evidence as unknown.
4. Apply bounded, already-authorized local edits. Ask only when release identity, historical correction, disclosure, or authority is materially unresolved; do not repeat confirmation for each edit within that authority.
5. Check the diff, duplicates, released history, fragment coverage, links, and applicable validators. Compare the current history with the DoD; repair authorized gaps and repeat affected checks with independent review/critique for material unresolved questions when available, otherwise sequential perspectives. Missing identity, evidence, or authority is incomplete with its next check.

Keep unrelated entries intact. Do not expose secrets, private paths, internal names, or embargoed details. Missing hosting access limits link verification; it does not block a safe local entry.

## Definition of Done

- The requested report, add, prepare, backfill, or repair mode and its evidence are explicit.
- Each changed entry is concise, public-safe, evidence-backed, and placed in the consumer's established history structure.
- Released history, unrelated entries, duplicates, links, and applicable validators have been checked.
- The result states remaining release work and does not claim a tag, hosted release, or publication occurred.
