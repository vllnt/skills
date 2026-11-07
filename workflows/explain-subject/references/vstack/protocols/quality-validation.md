## Contract

- Input: A current candidate, mode, validation contract, and evidence.
- Output: `PASS`, `REVISE`, or `BLOCKED`, with the risk tier, per-criterion proof, findings, and remaining work.
- Effects: Coordinates validation only. The caller owns candidate changes; a producer may add the smallest missing proof check.

### Acceptance

- The contract names the candidate, mode, criteria, unacceptable outcomes, risk tier, and a runnable proof for each applicable perspective.
- Each required criterion is pass, fail, or unverified, with run results bound to the current candidate.
- Independence matches the tier, or its absence is reported.
- Only reproduced, independently confirmed, or explicit-requirement findings block, and repair rounds stay within the cap.
- Authorized code changes pass a current reduction check that preserves contracts and renews affected proof.

## Procedure

1. Reuse the caller's validation contract. Record the candidate, mode, criteria, and unacceptable outcomes. Select only applicable perspectives, which the owning workflow or capability supplies (for code, the Code review plan table), and name a runnable proof for each. The caller assigns the risk tier; the highest matching tier wins, and a verifier may raise it but never lower it:
   - High: authentication or authorization, secrets, payments, data loss or migrations, concurrency, public contract breaks, production configuration.
   - Medium: any other behavior change, including user-visible or cross-module changes.
   - Low: mechanical, docs, or behavior-preserving change proven by existing or newly added checks.
2. When a required proof has no runnable check, the producer adds the smallest one at the project's existing owner (script, test, type or lint rule, benchmark, seed/reset, smoke driver, CI job) within authority. Prefer enforcement that makes the mistake impossible: types, then lint, then tests, then docs. When feasible, show the new check fails on the defect or pre-change behavior. Route broader tooling work to `improve-dx` when installed. Read-only modes propose the check. Build no tooling beyond the need.
3. Prove each criterion as pass, fail, or unverified with run results bound to the candidate. For authorized code changes, run a reduction pass before each commit or final uncommitted handoff: compare the whole task delta (commits, staged, unstaged, new files) with its verified baseline and apply justified deletion, reuse, consolidation, or a narrower change at the existing owner; justify retained complexity. Preserve features, compatibility, security, failure handling, meaningful test detection, and unrelated or mixed-owner edits. Uncertain attribution is a gap, not permission to delete; fewer lines, minification, hidden work, and deletion quotas are not success. Rerun invalidated checks; reuse current proof rather than repeat unchanged passes. Read-only work proposes reductions.
4. Verify independently by tier. Give each verifier checks within its tools and authority, and return missing required evidence to the caller.
   - Low: producer proof plus required checks and CI; report that no independent check ran.
   - Medium: an agent that did not produce the candidate reruns the proof, exercises the changed behavior or journey, and gives the diff one quick advisory review ([Code review](../capabilities/code-review/REFERENCE.md), review mode, quick depth).
   - High, or an explicit review request: medium plus a targeted review of the risk area or requested scope in review mode.
   - Non-code artifacts (plans, reports, explanations): self-assess against evidence and settle open forks with a prototype or discriminating check where the mode permits, else propose it. Use independent review only for high-tier decisions or on request.

   Without subagents, report missing independence; return `BLOCKED` only when the tier requires independence and none is available.
5. A finding blocks only if (1) a run on the current candidate reproduces it (failing test, command, or trace), (2) direct evidence shows a violated explicit requirement, or (3) a concrete failure scenario (inputs or state, wrong outcome) is confirmed by a second agent that did not raise it; all else is advisory. The caller arranges confirmation by an agent that neither produced the candidate nor raised the finding; it receives the scenario and candidate, not the raiser's verdict, and re-derives the failure, running it where possible. Record criterion, location or scenario, evidence, impact, bug class (so the producer fixes every instance), smallest remedy, and recheck. Tag each finding Important, Nit, or Pre-existing; pre-existing defects are reported but neither block nor count against it. Never repeat a finding from an earlier round; raise unchanged code only with new evidence. Tie each blocker to a current criterion or a demonstrated regression or safety obligation; evidence of a defect is separate from authority for its remedy. Honor accepted recovery paths, resolve conflicting requirements rather than silently strengthening or weakening either, and keep a disputed required criterion open. Deduplicate into required, optional, and rejected; each finding ends fixed, or rejected or deferred with a reason.
6. Make at most 3 repair rounds (5 for security or data-loss risk). After repairs, send affected verifiers the reason, revised material, and invalidated evidence; recheck only changed scope and invalidated proof. Stop when only optional findings remain. On unchanged evidence, change approach. At the cap, return `BLOCKED` with the unmet criterion, cause, options, recommendation, and consequence.
7. Return `PASS` only with proof for every required criterion and the tier's independence satisfied. Otherwise return `REVISE` for the caller to fix and resubmit, or `BLOCKED`.

## Pitfalls

- Green CI alone does not verify a behavior change.
- Unreproduced, unconfirmed findings never block.
- Low-tier self-proof is reported as self-proof.
- Consensus or a score never replaces proof.
