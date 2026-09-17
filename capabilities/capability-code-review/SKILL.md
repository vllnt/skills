---
name: capability-code-review
description: Assess a candidate diff for evidence-backed security, correctness, reliability, design, performance, cost, and delivery risks without repairing or approving it.
---

# Capability Code Review

Review a scoped candidate diff without editing, approving, merging, publishing, or submitting an external review.

## Procedure

1. Set base, candidate, scope, acceptance criteria, environment, and constraints. Read consumer rules, the complete diff, relevant callers, tests, and configuration.
2. Map changed entry points through contracts, state, consumers, and external effects. Assess applicable security, correctness, reliability, performance/cost, maintainability, developer experience, observability, and delivery perspectives.
3. Investigate supported boundaries, denial, retry, timeout, cancellation, concurrency, and recovery paths. Separate demonstrated defects, supported risks, and unanswered questions.
4. Deduplicate and rank findings. Each required finding includes location, scenario, evidence, impact, smallest repair, and verification; record exclusions and limitations.
5. When material risk or uncertainty remains, use independent review and critique perspectives when available; otherwise apply them sequentially. These perspectives assess this procedure; the caller owns overall convergence. For a new candidate or evidence, re-review affected findings and checks until defects in review evidence or candidate assessment resolve; blocked coverage yields the next check, and target-code repair is not required for a bounded review. Do not retry unchanged evidence; return the unresolved criterion and next discriminating check.

## Definition of Done

- Findings bind to the exact base, candidate, and reviewed scope.
- Checked perspectives and material exclusions are explicit.
- Every required finding is actionable and evidence-backed.
- A no-finding conclusion names reviewed scope, exclusions, and remaining risk.
