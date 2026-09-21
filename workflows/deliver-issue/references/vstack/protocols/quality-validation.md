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
3. For substantive work, use distinct subagents for review of correctness, completeness, and preserved behavior, and critique of assumptions, necessity, simplicity, and alternatives. Give each the same contract, candidate, evidence, and bounded scope. Use direct checks for mechanical work; without subagents, assess sequentially and report unavailable independence. If independent review is required but unavailable, return `BLOCKED`.
4. Collect verdicts and findings with criterion, location or scenario, evidence, impact, smallest remedy, and acceptance check. Deduplicate them into required fixes, selected improvements, optional suggestions, and justified rejections. Resolve disagreements with evidence; a disputed required criterion remains open.
5. Return actionable fixes to the caller. After every authorized revision, rerun invalidated checks and request fresh verdicts from affected reviewers and critics. Reuse only evidence and acceptance unaffected by the current candidate.
6. Return `PASS` only when every required criterion has proof, required perspectives accept their scopes, and no required finding remains. Otherwise return `REVISE` with fixes for the caller to implement and resubmit, or `BLOCKED` with the unmet criterion, cause, options, recommendation, and consequence. On unchanged evidence, change approach rather than retrying or lowering criteria.

## Pitfalls

- A reviewer consensus or numeric score cannot replace required evidence.
- Sequential assessment may inform the result but cannot satisfy a contract that requires independent review.
