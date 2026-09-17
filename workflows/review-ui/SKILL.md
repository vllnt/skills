---
name: review-ui
description: Assess an interface for evidence-backed usability, responsiveness, consistency, and accessibility findings without changing it.
---

# Review UI

Assess an interface and return findings only; do not repair, install, create hosted issues, or change external state.

## Workflow

1. Confirm the platform, screens, audience, task, candidate/environment, rules, evidence, bounded scope, and the mode-specific Definition of Done and proof from the request, applicable instructions, and loaded principles. Use only permitted read-only interaction.
2. Trace the main journey and applicable layout, content, feedback, loading, empty, error, validation, disabled, and success states.
3. Check platform-relevant interaction and accessibility. For web, inspect semantics, names, keyboard/focus, contrast, and motion; refer a requested full accessibility assessment to `capability-ui-accessibility` when available. Distinguish source, screenshot, automated, keyboard, and assistive evidence.
4. Return strengths and ordered findings with priority, location, state/viewport, impact, correction, and acceptance check; label preferences/hypotheses.
5. Validate the report against its declared coverage and criteria. Use `capability-quality-validation` when available; otherwise self-assess, use independent review and critique for substantive work, or assess perspectives sequentially and state unavailable independence; triage findings, revise the report or gather permitted evidence, and renew affected verdicts after a change. Use direct checks for mechanical work. On REVISE, continue report revision or permitted observation and fresh affected verdicts until acceptance. If a required correction is outside authority, return REVISE with the remedy and required checks. Return BLOCKED only when a required criterion cannot advance, with its next action; missing observation remains incomplete with its next check, and N/A needs a reason.

## Definition of Done

- Scope, candidate, task, and evidence types are identified.
- Main journey and platform-relevant states are assessed or excluded.
- Findings distinguish observations, preferences, and hypotheses.
- Unobserved interaction/accessibility gaps are explicit.
- Completion requires current validation acceptance for the report's declared coverage; otherwise report REVISE/BLOCKED with the unmet criterion and next action.
