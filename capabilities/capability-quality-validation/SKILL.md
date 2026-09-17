---
name: capability-quality-validation
description: Validate a candidate through predefined criteria, independent review and critique, triaged findings, and evidence-backed improvement loops.
---

# Capability Quality Validation

Validate one candidate for its caller. The caller owns changes and the requested endpoint; reviewers inspect without changing the target. Planning validates a plan, assessment validates a report, and implementation validates the changed artifact.

## Workflow

1. Before producing or revising a candidate, define the validation contract from the request, applicable user/project/nested instructions, loaded principles, and the owning workflow. Record candidate, mode, required criteria, evidence/checks, and useful review perspectives. Criteria must describe acceptable and unacceptable outcomes; unresolved criteria remain explicit. Reuse the caller's contract rather than inventing another.
2. Have the producer self-assess each criterion as pass, fail, or unverified with evidence. Fix known defects before independent review. A score may summarize a defined rubric; it cannot replace required proof.
3. For substantive work, use available subagents for distinct review and critique perspectives: reviewers test correctness, completeness, and preserved behavior; critics challenge assumptions, necessity, simplicity, and alternatives. Give them the same contract, candidate, evidence, and bounded scope. Use direct checks for mechanical work; without subagents, assess perspectives sequentially and report that independence was unavailable. If the contract requires independent review and it is unavailable, return BLOCKED; sequential assessment cannot satisfy that criterion. Do not spawn recursive review pools.
4. Collect each perspective's verdict and findings: criterion, location/scenario, evidence, impact, smallest remedy, and acceptance check. The coordinator deduplicates and records required fixes, selected improvements, optional suggestions, and justified rejections. Resolve disagreement with evidence, not votes; a disputed required criterion remains open until resolved.
5. Return actionable fixes to the caller for authorized improvement. After each revision, rerun invalidated checks and request fresh verdicts from affected reviewers and critics. Reuse only unaffected evidence and acceptance tied to the current candidate; do not restart the whole pool unnecessarily.
6. Return PASS only when every required criterion has proof, required perspectives have accepted within their scopes, and no required finding remains. Otherwise return REVISE with actionable fixes for the caller to implement and resubmit while authorized and feasible, or BLOCKED with the unmet criterion, cause, viable options, recommendation, and consequence. Continue useful independent work; on unchanged evidence, change approach rather than retry or lower the criteria. Change a contract only for an explicit scope change or a justified correction, then revalidate affected work.

## Definition of Done

- The contract identifies the candidate, mode, applicable rules, required criteria, evidence, and perspective coverage before evaluation.
- Self-assessment, review, critique, and finding dispositions are traceable; unavailable independence and missing proof are explicit.
- PASS is supported by current evidence and scoped acceptance; REVISE or BLOCKED identifies the remaining work without claiming validation.
- Authorized revisions receive renewed affected checks and verdicts; the caller retains mutation and endpoint ownership.
