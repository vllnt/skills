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
3. For substantive work, have reviewers independent of the producer review correctness, completeness, and preserved behavior, and critique assumptions, necessity, simplicity, and alternatives. One reviewer may cover both perspectives; use additional reviewers only for required separation or non-overlapping scopes reviewed in parallel. Provide assigned criteria, the candidate or relevant diff, and current evidence. Assign only checks supported by each reviewer's tools and authority; return missing required evidence to the caller, not a passing verdict. Use direct checks for mechanical work; without subagents, assess sequentially and report unavailable independence. If independent review is required but unavailable, return `BLOCKED`.
4. Collect verdicts and findings with criterion, location or scenario, evidence, impact, smallest remedy, and acceptance check. Deduplicate them into required fixes, selected improvements, optional suggestions, and justified rejections. Resolve disagreements with evidence; a disputed required criterion remains open.
5. Return actionable fixes to the caller. After each authorized revision, provide affected reviewers the finding or reason for change, revised candidate or relevant diff, and invalidated evidence. Rerun invalidated checks and renew affected verdicts. Reuse only evidence and acceptance unaffected by changes to the candidate, inputs, or relevant environment.
6. Return `PASS` only when every required criterion has proof, required perspectives accept their scopes, and no required finding remains. Otherwise return `REVISE` with fixes for the caller to implement and resubmit, or `BLOCKED` with the unmet criterion, cause, options, recommendation, and consequence. On unchanged evidence, change approach rather than retrying or lowering criteria.

## Pitfalls

- A reviewer consensus or numeric score cannot replace required evidence.
- Sequential assessment may inform the result but cannot satisfy a contract that requires independent review.
