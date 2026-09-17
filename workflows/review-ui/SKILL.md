---
name: review-ui
description: Assess an interface for evidence-backed usability, responsiveness, consistency, and accessibility findings without changing it.
---

## Goal

Assess an interface and return evidence-backed findings without changing it.

### Definition of Done

- Scope, candidate, environment, task, and evidence types are identified.
- The main journey and platform-relevant states are assessed or explicitly excluded.
- Findings distinguish observations, preferences, and hypotheses and include priority, location, impact, correction, and acceptance check.
- Unobserved interaction and accessibility gaps are explicit.
- Current validation accepts the report's declared coverage; no required finding remains.

## Boundaries

- Do not repair the interface, install anything, create hosted issues, or change external state. A missing observation is incomplete, not a pass; N/A needs a reason.

## Workflow

1. Resolve platform, screens, audience, task, candidate/environment, rules, permitted read-only evidence, bounded scope, and validation criteria.
2. Trace the main journey and applicable layout, content, feedback, loading, empty, error, validation, disabled, and success states.
3. Check platform-relevant interaction and accessibility. For web, inspect semantics, names, keyboard/focus, contrast, and motion; in review mode, use `capability-ui-accessibility` when an expanded assessment is required. Distinguish source, screenshot, automated, keyboard, and assistive evidence.
4. Return strengths and ordered findings with evidence, priority, location, state or viewport, impact, correction, and acceptance check.
5. For a substantive report, run the quality-validation loop. Revise only the report or gather permitted evidence, then renew affected verdicts until the declared coverage is accepted.
