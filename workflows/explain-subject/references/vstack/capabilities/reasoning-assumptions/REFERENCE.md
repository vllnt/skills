## Contract

- Input: A real subject, decision or claim under test, supporting evidence, and material constraints.
- Output: An evidence-backed assessment with an assumption ledger, primitives, rebuilt result, observable checks, and remaining uncertainty.
- Effects: Analysis only. The result does not authorize implementation.

### Acceptance

- The subject, decision, and material constraints are explicit.
- Every material assumption has a classification, evidence, uncertainty, and consequence.
- The rebuilt result follows decision-relevant primitives and names observable checks for material claims.
- The output separates facts, assumptions, and unknowns.

## Procedure

1. Frame the information need, job to be done, or claim under test. Identify the candidate and material constraints.
2. List assumptions and classify each as real, inherited, or unknown, with evidence and cost of being wrong.
3. Reduce real constraints into independent decision-relevant primitives. Retain a convention only when evidence still justifies its purpose.
4. Rebuild the explanation, design, or decision from those primitives. Compare alternatives when they affect the result, then recommend the smallest reversible choice supported by evidence.
5. Give each material primitive an observable check: metric or acceptance condition, evidence source, and goal-relative threshold when known.
6. Return the frame, ledger, primitives, rebuilt result, discarded conventions, and changing evidence. For consequential unresolved choices, state options, recommendation, impact, and required decision. Correct authorized analysis errors and recheck affected claims; send material contested claims and proof to the caller's Quality Validation pool.

## Pitfalls

- Convention is not a binding constraint. Verify its purpose before preserving it.
- Do not present an unknown threshold or unfamiliar fact as established; name the next decisive check.
