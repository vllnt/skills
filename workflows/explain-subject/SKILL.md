---
name: explain-subject
description: Explain a real subject with a simple verified mental model and clear limits.
---

## Goal

Explain a real subject so the reader can reason about or decide on it.

### Definition of Done

- The subject, depth, and decision served are explicit.
- The overview, map, and explanation address that decision.
- Facts are sourced or labeled uncertain; analogies state their limits.
- Current validation accepts the explanation or names the unresolved claim and next verifying source.

## Boundaries

- Do not present simplifications, assumptions, or unverified claims as facts.

## Workflow

1. Resolve the subject, depth, intended decision, applicable instructions, and required evidence.
2. Inspect relevant code or authoritative sources for uncertain material facts.
3. Give one true overview, the smallest useful map, and plain-language explanations. Use an analogy only when it clarifies the decision.
4. Self-assess the factual claims. For assumption-heavy or consequential reasoning, use [Reasoning assumptions](references/vstack/capabilities/reasoning-assumptions/REFERENCE.md) with the advisory mode, scope, candidate, and evidence. For substantive explanations, use [Quality validation](references/vstack/protocols/quality-validation.md) in advisory, read-only mode with those findings; if unavailable, self-assess, collect review and critique, triage corrections, and renew affected verdicts directly.
5. Return sources, assumptions, simplifications, gaps, and the next verifying source for any unresolved claim.
