## Contract

- Input: A current candidate, mode, validation contract, evidence, and required review or critique perspectives.
- Output: `PASS`, `REVISE`, or `BLOCKED`, with traceable evidence, verdicts, findings, and remaining work.
- Effects: Coordinates validation only. The caller owns candidate changes and the requested endpoint.

### Acceptance

- The contract identifies the candidate, mode, applicable rules, criteria, evidence, and perspective coverage before evaluation.
- Self-assessment, review, critique, and finding dispositions are traceable.
- `PASS` has current proof and scoped acceptance; missing independence or proof remains explicit.
- Authorized revisions receive renewed affected checks and verdicts.

## Procedure

1. Reuse the caller's validation contract. Record candidate, mode, required criteria, evidence or checks, unacceptable outcomes, and useful review perspectives from the request, applicable instructions, principles, and owning workflow.
2. Have the producer self-assess each criterion as pass, fail, or unverified with evidence. Return known defects to the caller before independent review. A score may summarize a defined rubric but cannot replace required proof.
3. For substantive work, obtain review of correctness, completeness, and preserved behavior, and critique of assumptions, necessity, simplicity, and alternatives from reviewers independent of the producer. One reviewer may cover both; add reviewers only for required separation or non-overlapping parallel scopes. Supply scoped criteria, the candidate or diff, and current evidence. Assign checks within each reviewer's tools and authority; return missing required evidence to the caller. Use direct checks for mechanical work. Without subagents, assess sequentially and report missing independence; return `BLOCKED` if required independent review is unavailable.
4. Collect verdicts and findings with criterion, location or scenario, evidence, impact, smallest remedy, and acceptance check. Deduplicate them into required fixes, selected improvements, optional suggestions, and justified rejections. Resolve disagreements with evidence; a disputed required criterion remains open.
5. Return fixes to the caller. After authorized revisions, send affected reviewers the reason, revised material, and invalidated evidence. Rerun invalidated checks and renew affected verdicts; retain only evidence and acceptance unaffected by changes to the candidate, inputs, or relevant environment.
6. Return `PASS` only when every required criterion has proof, required perspectives accept their scopes, and no required finding remains. Otherwise return `REVISE` with fixes for the caller to implement and resubmit, or `BLOCKED` with the unmet criterion, cause, options, recommendation, and consequence. On unchanged evidence, change approach rather than retrying or lowering criteria.

## Pitfalls

- A reviewer consensus or numeric score cannot replace required evidence.
- Sequential assessment may inform the result but cannot satisfy a contract that requires independent review.
