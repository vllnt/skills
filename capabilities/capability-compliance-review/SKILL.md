---
name: capability-compliance-review
description: Audit a website or web app for evidence-backed privacy, accessibility, consumer, and AI-content compliance risks without certifying compliance.
---

## Contract

- Input: Consumer rules, source, policies, configuration, authorized runtime evidence, target, jurisdictions, users, data, commerce, and AI/UGC features.
- Output: Applicability matrix, prioritized technical findings, evidence state, remediation, verification, and coverage gaps.
- Effects: Read-only technical audit. It is not legal advice or a compliance certification.

### Acceptance

- The applicability matrix and scope limitations are present.
- Findings distinguish live evidence, source evidence, and unverified controls.
- Severity applies only to evidenced, applicable risk.
- The conclusion names audited controls, `UNVERIFIED` limits, and makes no certification claim.

## Procedure

1. Read consumer rules, source, policies, configuration, and authorized runtime evidence. Set target, jurisdictions, users, data, commerce, AI/UGC features, and safe test methods. Use isolated fixtures; do not make real purchases, send messages, grant consent, or change accounts.
2. Decide applicability before auditing. Mark uncertain jurisdiction or service scope `APPLIES?`; use current authoritative sources when law or guidance may have changed.
3. Load only relevant [privacy](references/privacy.md), [accessibility](references/accessibility.md), [consumer](references/consumer.md), and [AI/content](references/ai-content.md) checks.
4. For each applicable finding, report severity, location, observed/source/unverified evidence, impact, owner, smallest remediation, and verification. `PASS` applies only to the observed check.
5. Return material uncertainties and current evidence to the caller's quality validation. When standalone, return `UNVERIFIED` with the next check. Reassess affected controls after changed evidence or authorized remediation; escalate high-severity legal interpretation to counsel.

## Pitfalls

- A policy page does not prove live control behavior; identify it as source evidence until a safe observation confirms it.
- An uncertain jurisdiction does not establish applicability; retain `APPLIES?` and obtain authoritative guidance.
