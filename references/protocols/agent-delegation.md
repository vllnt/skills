## Contract

- Input: A requested outcome, mode, authority, validation contract, available agent roles and runtimes, and the current capacity level.
- Output: Consolidated results with evidence paths, decisions, open issues, and the reached endpoint.
- Effects: Coordinates delegated work and closes only the sessions it started. The manager owns decisions and the requested endpoint; each worker owns only its assigned scope.

### Acceptance

- One manager plans, decides, and consolidates, reading only the evidence each decision needs; workers perform the bulk reading, coding, testing, and summarizing.
- Every worker has one narrow scope and clear ownership; no two concurrent workers own the same files or decisions.
- Briefs and reports are short and traceable; raw logs and transcripts stay out of the manager's context.
- Fan-out stays within the current [Capacity gating](capacity-gating.md) level.
- Idle workers, sessions, and processes the manager started are closed or handed off before completion.

## Procedure

1. Assign roles per consumer rules: a capable planner model as manager and the cheapest worker subagent adequate for each scope. Keep a quick answer, a single lookup, a decision, or an approval in the manager; delegate anything beyond about two tool calls.
2. Split the work by ownership before spawning: one file area, module, investigation, or review angle per worker. Run independent scopes in parallel within the level from [Capacity gating](capacity-gating.md); serialize scopes that share files or depend on each other's output.
3. Brief each worker with the goal, owned scope, inputs or paths, constraints, mode, and done criteria. Tell it to proceed without stopping for routine questions, to escalate only missing authority or consequential ambiguity, and to end with a compact report: result, evidence paths, checks run, and open issues. Do not forward the full conversation or catalog.
4. Run a session manager or terminal multiplexer, when one is used, through its supported interface. Use one workspace per task, read identifiers from command output instead of guessing, and inspect delivery before resubmitting a prompt that may have been received.
5. Validate through [Quality validation](quality-validation.md); the manager supplies the validation contract and consolidates its report.
6. Spend tokens on decisions, not traffic:
   - Keep manager turns to orchestration and batch related requests into one brief.
   - Wait on completion events or a single blocking wait; do not poll in a loop.
   - Send terse messages without acknowledgement-only replies; mark messages urgent only when the recipient must act.
   - Run scheduled checks at the longest interval that meets the need; stay quiet unless something changed.
   - Read selectively: reports, bounded tails, and targeted searches, never whole logs or transcripts.
   - Reuse a worker's proof while its candidate, inputs, and environment remain valid; re-verify only what changed, conflicts, or looks wrong.
7. Steer an existing worker rather than starting a duplicate. When a worker is blocked on an approval or question, read it and answer within the manager's authority; escalate only what exceeds it. Close the workspaces, sessions, and processes you created when their work is merged, handed off, or abandoned; never close another owner's sessions.

## Role routing

Use the highest reasoning effort the runtime offers for every role.

- **Check availability first:** check provider/account availability and quota before routing; fall back to another provider when one is exhausted or rate-limited, and spread load across available accounts.
- **Builder** (default): routine code, fixes, refactors, tests, docs, review fixes, and bulk work, as narrowly scoped workers.
- **Planner/manager:** multi-file and long-running goals, plans, architecture, and requirements; fans work out to parallel builders.
- **Outside critic:** a model from a different provider or family, used to challenge and review, never as the main builder.
  - Plan challenge before implementation.
  - Independent diff review alongside parallel per-angle builder reviewers, consolidated into one report before merge.
  - Root-cause analysis for hard bugs and incidents; the planner verifies.
  - Security, infrastructure, data, and migration changes: the planner plans, the critic approves before execution, a builder executes.
  - Business, pricing, and finance reasoning: the planner drafts, the critic challenges the numbers.
- **Escalation:** builder stuck after two attempts → planner → critic.
- **Priority tiers:** urgent work runs in parallel immediately with critic review after shipping; normal work follows this routing; low-priority work uses builders only, and only with spare capacity.
- **Capacity gate:** run [Capacity gating](capacity-gating.md) before large sessions and cap parallel builders to the available headroom.
- **Goal-prompt checklist:** every long-running goal prompt states the applicable critic steps: plan challenge before implementing, independent review before merge, critic root cause after two failed fix attempts, and critic approval before security, infrastructure, data, or migration execution.

## Pitfalls

- A queued or delivered prompt is not proof of work; confirm state from the session or report.
- An idle or done session does not prove its background subtasks finished; check their reports.
- If every worker runtime is unavailable or rate-limited, report the blocker to the runtime owner, or the requester when unknown, and wait; do not bypass the configured interface.
