## Contract

- Input: Current candidate, mode, validation contract, evidence.
- Output: `PASS`, `REVISE` (caller repairs), or `BLOCKED`, with tier, proof, findings.
- Effects: Validation only. The caller owns changes; a producer may add the smallest missing check or reduction (read-only modes propose them).

### Acceptance

- Criteria, unacceptable outcomes, tier, and runnable proof are named; each criterion passes, fails, or stays unverified, with run results bound to the candidate.
- Independence matches the tier or its absence is reported.
- Only findings meeting the blocking rule block, within the repair cap; authorized code passes a current reduction pass that preserves contracts.

## Procedure

1. Reuse the caller's contract and applicable perspectives, each with runnable proof. The caller assigns the tier (highest match wins); verifiers may raise, never lower it. Verifiers stay within their tools and authority, returning gaps. No subagents: report missing independence; `BLOCKED` if the tier requires independence.
   - Low (mechanical, docs, or behavior-preserving, proven by existing or new checks): producer proof, required checks, CI; report no independent check.
   - Medium (any other behavior change): a non-producer reruns the proof, exercises the change, and gives the diff a quick advisory review (code review, quick depth, if linked; else read the diff inline).
   - High (auth, secrets, payments, data loss, migrations, concurrency, public contract breaks, production config) or an explicit review request: medium plus a targeted review of the risk area or requested scope.
   - Non-code artifacts: self-assess; where the mode permits, settle open forks with a prototype or discriminating check, else propose it; independent review only at high tier or on request.
2. Missing runnable proof: the producer adds the smallest check at the existing owner within authority (types > lint > tests > docs), failing first when feasible; broader tooling goes to `improve-dx` when installed.
3. Before committing or handing off authorized code, reduce: compare the whole task delta with its verified baseline; apply justified deletion, reuse, consolidation, or narrowing at the existing owner; justify what stays. Preserve supported behavior, security, failure handling, test detection, and unrelated edits; line count is not success; uncertain attribution is a gap, not permission to delete. Rerun invalidated checks.
4. A finding blocks only if a run on the candidate reproduces it, it violates an explicit requirement, or an agent that neither produced the candidate nor raised it confirms a concrete failure scenario, re-derived without the raiser's verdict.
5. Ledger per finding: criterion, location/scenario, evidence, impact, bug class (fix every instance), smallest remedy, recheck; tag Important, Nit, or Pre-existing (never blocking). No repeats without new evidence. Each ends fixed, rejected, or deferred, with reason. Blockers need a current criterion, demonstrated regression, or safety obligation; defect evidence is not remedy authority. Honor accepted recovery paths; resolve conflicting requirements without weakening either; keep a disputed criterion open.
6. At most 3 repair rounds (5 for security or data loss). Send verifiers revised material and invalidated evidence; recheck only those. Stop at optional-only findings; change approach on unchanged evidence. At the cap, `BLOCKED` with the unmet criterion, cause, options, recommendation, consequence.
