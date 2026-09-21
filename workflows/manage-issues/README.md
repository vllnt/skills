# Manage Issues

Turn a bounded backlog into an evidence-backed queue. It recommends the first coherent slice, then applies only authorized changes.

## What it does

| Capability | Result |
|---|---|
| Stale detection | Flags issues whose relevance needs review under the consumer policy |
| Documentation alignment | Checks each issue against the repository's discovered sources of truth; flags drift both ways |
| Merge | Dedupes near-duplicates — canonical kept, dups closed as `duplicate` (reopenable; no native merge exists) |
| Split | Breaks compound issues into atomic sub-issues — **one problem, one issue** |
| Quality gate | Checks that each issue can be picked up without guessing |
| Parallelize | Dependency graph → ready-now set, bottlenecks, independent lanes for concurrent work |

## Safety

- Read-only requests never write; authorized changes apply only to the requested subset.
- Never deletes an issue — closes with a reason and a cross-link (reopenable).
- Stale handling follows the consumer policy. Splits never lose content. Bulk operations are previewed.
- Reads the authoritative documentation it discovers but does not edit it as a triage side effect.

See [SKILL.md](SKILL.md) and load references only for the requested operation.
