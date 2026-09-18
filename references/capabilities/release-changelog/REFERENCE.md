## Contract

- Input: A requested history operation, consumer release rules, current history, and evidence for the change.
- Output: A verified report or bounded local history update, with remaining release work.
- Effects: Owns the existing changelog and pending entries. Does not own version manifests, tags, hosted releases, or publishing.

### Acceptance

- The requested report, add, prepare, backfill, or repair mode and evidence are explicit.
- Every changed entry is concise, public-safe, evidence-backed, and in the established history structure.
- Released history, unrelated entries, duplicates, links, and applicable validators have been checked.
- The result does not claim a tag, hosted release, or publication occurred.

## Procedure

1. Read consumer instructions, history, release process, and evidence. Set the history owner and operation. Reuse the established `[Unreleased]` section, fragments, or generator; use [format examples](references/format.md) only when no format exists.
2. Apply the selected operation: report reads only; add writes one pending outcome; prepare promotes only approved entries into the approved version and date; backfill adds evidenced omissions; repair corrects authorized structural drift without rewriting released meaning.
3. Use public-safe, evidence-backed wording. Treat a commit subject as a lead, not behavior proof; mark uncertain shipment, version, date, or link evidence as unknown.
4. Apply bounded authorized local edits. Ask only for materially unresolved release identity, historical correction, disclosure, or authority.
5. Check the diff, duplicates, released history, fragment coverage, links, and applicable validators. Repair authorized gaps and repeat affected checks. Send material unresolved questions and proof to the caller's Quality Validation pool. Return incomplete work with its next check when identity, evidence, or authority is missing.

## Pitfalls

- A commit title does not prove user-visible behavior, shipment, or publication. Use supporting evidence or mark it unknown.
- Do not expose secrets, private paths, internal names, or embargoed details in public history.
