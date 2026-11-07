## Contract

- Input: Mode (`plan` or `review`), base, candidate, scope, and criteria; for review, the depth (`quick` for medium risk, `targeted` for high risk or an explicit review request) and the diff, callers, tests, and configuration.
- Output: Plan mode returns applicable perspectives with a runnable proof each and proof checks to add. Review mode returns ranked findings tagged Important, Nit, or Pre-existing, each with bug class and reproduction or scenario, plus exclusions, limitations, and next checks.
- Effects: Plan mode is read-only. Review mode never edits product code, approves, merges, publishes, or submits an external review; where the caller permits writes it may add a failing evidence test (caller-owned), otherwise it describes the reproduction as steps or a command.

### Acceptance

- Plan mode names each applicable perspective, its runnable proof, and any proof check to add.
- Review covers only the stated depth and scope, with findings bound to the exact base and candidate.
- A no-finding conclusion names scope, exclusions, and remaining risk.

## Procedure

1. Read consumer rules and the relevant contracts, callers, tests, and configuration.
2. Plan mode: select the perspectives the change's risk makes applicable; name each one's runnable proof and any proof check to add at the project's existing owner.

   | Perspective | Proof | Applies when |
   |---|---|---|
   | Correctness | Tests of changed behavior and failure paths | Always |
   | Security | Denial or authorization test, secret scan, dependency audit | Auth, input, data access |
   | Performance | Benchmark against base, size budget | Hot paths, rendering, queries |
   | Scalability | Query-count or N+1 test; load test if relevant | Loops over data, new endpoints |
   | Observability | Test that entry points emit logs, metrics, or traces | New entry points, jobs, error paths |
   | Reliability | Timeout, retry, and failure tests | External calls, queues |
   | Compatibility | Contract or consumer test | Public APIs, schemas |
   | Maintainability | Reduction pass, lint, types | Always |
   | Accessibility | Automated check plus keyboard path | UI |
3. Review mode. Quick: read the diff once against the applicable perspectives. Targeted: review only the risk area or requested scope, mapping entry points through contracts, state, consumers, and external effects and probing boundaries, denial, retry, timeout, cancellation, concurrency, and recovery; separate demonstrated defects, supported risks, and open questions.
4. Propose a block only per the caller's quality validation: a reproduction (a failing evidence test or steps, per Effects), a violated explicit requirement, or a concrete failure scenario for an uninvolved agent to re-derive without your verdict. Record location, scenario, evidence, impact, bug class (fix every instance), smallest repair, and verification; skip earlier-round repeats. A maintainability finding also needs evidenced cost and a simpler alternative. Do not repair product code. Deduplicate and rank.
5. Return risks and evidence to the caller's quality validation (standalone: coverage gaps and next check); re-review only affected findings.
