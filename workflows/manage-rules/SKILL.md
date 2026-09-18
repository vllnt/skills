---
name: manage-rules
description: Manage user, project, and nested instructions while preserving scope, precedence, and effective behavior.
---

## Goal

Give each user, project, or nested rule one clear owner while preserving scope, precedence, and effective behavior.

### Definition of Done

- Sources, scope, precedence, consumers, authority, and evidence status are explicit.
- Assessment returns an owned repair proposal and expected effect without edits or effectful probes.
- Authorized changes preserve unrelated and protective rules with representative before/after scope evidence.
- Unknown precedence or reach is explicit.
- Current validation accepts the selected mode; no required finding remains.

## Boundaries

- Do not assume that an instruction link loads or that repository rules override higher authority. Report runtime-observed, source-simulated, and unknown precedence separately.

## Workflow

1. Discover active instruction sources, scopes, activation, imports, authority, consumers, and edit permission without scanning unrelated private projects.
2. Compare only overlapping scopes. Classify duplicate, contradiction, deliberate override, and unrelated wording.
3. Choose the smallest repair: keep user preferences at user scope, project decisions at project scope, and exceptions narrow.
4. For substantive candidates, use [Quality validation](references/vstack/protocols/quality-validation.md) with the mode, scope, candidate, and evidence; otherwise apply its feedback loop directly before authorized edits. Triage findings, improve the candidate, and renew affected verdicts until acceptance.
5. Apply only authorized validated edits, preserve unrelated or protective rules, and test representative scope behavior where bounded.
