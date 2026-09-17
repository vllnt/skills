# Review

Verify the result and completion criteria. Use independent subagents when available, following [coordination](coordination.md).

| Perspective | Check |
|---|---|
| Contract | Trigger, inputs, effects, mode-specific DoD, and consumer-policy ownership. |
| Composition | Callers, links, fallback, cycles, duplicate responsibilities, and deletion compatibility. |
| Behavior | Success/failure, missing tools, changed data without skill edits, invalidated proof, and blocked completion. |

1. Identify the candidate and assigned scope.
2. Exercise relevant scenarios and two contrasting consumer configurations; distinguish simulation from execution.
3. Return supported defects and concrete remedies in the [finding format](coordination.md#finding-format), or accept when none remain.
