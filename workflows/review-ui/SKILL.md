---
name: review-ui
description: Assess an interface for evidence-backed usability, responsiveness, consistency, and accessibility findings without changing it.
---

# Review UI

Assess an interface and return findings only; do not repair, install, create hosted issues, or change external state.

## Workflow

1. Confirm the platform, screens, audience, task, candidate/environment, rules, evidence, and bounded scope. Use only permitted read-only interaction.
2. Trace the main journey and applicable layout, content, feedback, loading, empty, error, validation, disabled, and success states.
3. Check platform-relevant interaction and accessibility. For web, inspect semantics, names, keyboard/focus, contrast, and motion; refer a requested full accessibility assessment to `capability-ui-accessibility` when available. Distinguish source, screenshot, automated, keyboard, and assistive evidence.
4. Return strengths and ordered findings with priority, location, state/viewport, impact, correction, and acceptance check; label preferences/hypotheses.
5. When material risk or uncertainty remains, use distinct review and critique perspectives when available; otherwise assess them sequentially. Close analysis gaps with permitted observation or source review and recheck affected evidence. Missing observation remains incomplete with its next check; N/A needs a reason.

## Definition of Done

- Scope, candidate, task, and evidence types are identified.
- Main journey and platform-relevant states are assessed or excluded.
- Findings distinguish observations, preferences, and hypotheses.
- Unobserved interaction/accessibility gaps are explicit.
