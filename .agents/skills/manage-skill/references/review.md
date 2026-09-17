# Review

Verify the result and completion criteria. Use independent subagents when available, following [coordination](coordination.md).

| Perspective | Check |
|---|---|
| Contract | Trigger, family structure, inputs, effects, acceptance evidence, and consumer-policy ownership. |
| Composition | Callers, links, fallback, cycles, duplicate responsibilities, and deletion compatibility. |
| Behavior | Success/failure, missing or contradictory evidence, unavailable tools, unintended writes, stale proof, and blocked completion. |

1. Identify the candidate and assigned scope.
2. Exercise relevant scenarios; compare contrasting consumer configurations when behavior depends on them. Distinguish simulation from execution.
3. Return supported defects and concrete remedies in the [finding format](coordination.md#finding-format), or accept when none remain.
