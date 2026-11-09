## Contract

- Input: Mode (`plan` or `review`), base, candidate, scope, acceptance criteria, environment, and constraints; for review, the depth (`quick` for medium risk, `targeted` for high risk or an explicit review request) and the risk area or requested scope with its diff, callers, tests, and configuration.
- Output: Plan mode returns the applicable perspectives, a runnable proof for each, and any proof check to add. Review mode returns ranked findings, each tagged Important, Nit, or Pre-existing with its bug class and reproduction or scenario, plus exclusions, limitations, and next checks.
- Effects: Plan mode is read-only planning output. Review mode never edits product code, approves, merges, publishes, or submits an external review; where the caller's mode permits writes it may add a failing evidence test with the candidate's tests, which the caller owns keeping or removing, and otherwise it describes the reproduction as steps or a command.

### Acceptance

- Plan mode names each applicable perspective, its runnable proof, and whether a proof check must be added.
- Review mode covers only the stated depth and scope; findings bind to the exact base, candidate, and scope.
- Every blocking finding is reproduced, shows a violated explicit requirement, or is a concrete failure scenario confirmed by a second agent that did not raise it; all others are advisory.
- A no-finding conclusion names reviewed scope, exclusions, and remaining risk.

## Procedure

1. Set the mode, base, candidate, scope, acceptance criteria, environment, and constraints. Read consumer rules and the relevant contracts, callers, tests, and configuration.
2. Plan mode, for the producer at planning and implementation time: select the perspectives below that the change's risk makes applicable. For each, name the runnable proof and whether a proof check must be added at the project's existing owner.

   | Perspective | Proof | Applies when |
   |---|---|---|
   | Correctness | Tests of changed behavior and failure paths | Always |
   | Security | Denial or authorization test, secret scan, dependency audit | Auth, input handling, data access |
   | Performance | Benchmark against base, bundle or size budget | Hot paths, rendering, queries |
   | Scalability | Query-count or N+1 test; load test only when relevant | Loops over data, new endpoints |
   | Observability | Test that new entry points emit structured logs, metrics, or traces | New entry points, jobs, error paths |
   | Reliability | Timeout, retry, and failure tests | External calls, queues |
   | Compatibility | Contract or consumer test | Public APIs, schemas |
   | Maintainability | Reduction pass, lint, types | Always |
   | Accessibility | Automated accessibility check plus keyboard path | UI |
3. Review mode. Quick depth, for a medium change: read the diff once against the applicable table perspectives and return findings without deep investigation; they follow step 4's blocking rule. Targeted depth, for a high-tier change or an explicit review request: review only the risk area or requested scope, with the perspectives it names or the change's risk selects from the table. Map its entry points through contracts, state, consumers, and external effects, and investigate boundaries, denial, retry, timeout, cancellation, concurrency, and recovery. Separate demonstrated defects, supported risks, and unanswered questions. Without subagents, run the perspectives sequentially and report missing independence.
4. Give each finding you propose to block on a reproduction (a failing evidence test where the caller permits writes, otherwise steps or a command), direct evidence of a violated explicit requirement, or a concrete failure scenario (inputs or state, wrong outcome) for the caller to have an agent that neither produced the candidate nor raised the finding re-derive without your verdict; otherwise mark it advisory. Tag it Important, Nit, or Pre-existing (reported, never blocking), name its bug class so every instance is fixed, and do not repeat findings from earlier rounds. Include location, scenario, evidence, impact, smallest repair, and verification. A maintainability finding also needs an evidenced maintenance cost and a concrete simpler alternative that preserves supported contracts. Do not repair product code. Deduplicate and rank.
5. Return material risks, uncertainties, and current evidence to the caller's quality validation. When standalone, return coverage gaps and the next check. Re-review only affected findings for a new candidate or evidence.

## Pitfalls

- Counts, a single caller, unfamiliar structure, or missing usage evidence do not establish redundancy. Inspect supported consumers and boundary responsibilities; distinguish project requirements from style preferences.
- A passing test outside the changed contract does not clear a finding; bind the test, base, candidate, and scenario.
- Absence of findings is not approval; report exclusions and remaining risk.
