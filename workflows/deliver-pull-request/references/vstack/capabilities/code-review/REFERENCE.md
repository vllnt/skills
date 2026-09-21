## Contract

- Input: Base, candidate, scope, acceptance criteria, environment, constraints, complete diff, callers, tests, and configuration.
- Output: Ranked actionable findings, reviewed perspectives, exclusions, limitations, and next checks.
- Effects: Read-only review. It does not edit, approve, merge, publish, or submit an external review.

### Acceptance

- Findings bind to the exact base, candidate, and reviewed scope.
- Checked perspectives and material exclusions are explicit.
- Every required finding is actionable and evidence-backed.
- A no-finding conclusion names reviewed scope, exclusions, and remaining risk.

## Procedure

1. Set the base, candidate, scope, acceptance criteria, environment, and constraints. Read consumer rules, the complete diff, relevant callers, tests, and configuration.
2. Map changed entry points through contracts, state, consumers, and external effects. Assess applicable security, correctness, reliability, performance/cost, maintainability, developer experience, observability, and delivery. Compare added or retained complexity with deletion, reuse, or consolidation. Require an evidenced maintenance cost and a concrete simpler alternative preserving supported contracts before making simplification a required finding.
3. Investigate supported boundaries, denial, retry, timeout, cancellation, concurrency, and recovery. Separate demonstrated defects, supported risks, and unanswered questions.
4. Deduplicate and rank findings. Each required finding includes location, scenario, evidence, impact, smallest repair, and verification.
5. Return material risks, uncertainties, and current evidence to the caller's quality validation. When standalone, return coverage gaps and the next check. Re-review only affected findings for new candidate or evidence; a bounded review can complete without target-code repair.

## Pitfalls

- Counts, a single caller, unfamiliar structure, or missing usage evidence do not establish redundancy. Inspect supported consumers and boundary responsibilities; distinguish project requirements from style preferences.
- A passing test outside the changed contract does not clear a finding; bind the test, base, candidate, and scenario.
- Absence of findings is not approval; report exclusions and remaining risk.
