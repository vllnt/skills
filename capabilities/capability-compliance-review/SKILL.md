---
name: capability-compliance-review
description: Audit a website or web app for evidence-backed privacy, accessibility, consumer, and AI-content compliance risks without certifying compliance.
---

# Capability Compliance Review

Assess technical evidence against potentially applicable requirements. It is a read-only technical audit, not legal advice or a compliance certification.

## Procedure

1. Read consumer rules, source, policies, configuration, and authorized runtime evidence. Set target, jurisdictions, users, data, commerce, AI/UGC features, and safe test methods.
2. Decide applicability before auditing. Mark uncertain jurisdiction or service scope `APPLIES?`; use current authoritative sources when law or guidance may have changed.
3. Load only relevant [privacy](references/privacy.md), [accessibility](references/accessibility.md), [consumer](references/consumer.md), and [AI/content](references/ai-content.md) checks. Use safe test identities and never submit real purchases, messages, consent, or account changes.
4. For each applicable finding, report severity, location, observed/source/unverified evidence, impact, owner, smallest remediation, and verification. `PASS` applies only to the observed check.
5. For material unresolved questions, use independent review and critique when available; otherwise assess sequentially. Reuse relevant caller evidence while current. For revised evidence or an authorized remediation, reassess affected controls and safe checks until assessment findings resolve; high-severity legal interpretation goes to counsel, while blocked access is `UNVERIFIED` with the next check. Do not retry unchanged evidence; return the unresolved criterion and next discriminating check.

## Definition of Done

- The applicability matrix and scope limitations are present.
- Findings distinguish live evidence, source evidence, and unverified controls.
- Severity is used only for evidenced, applicable risk.
- The conclusion names the audited controls, `UNVERIFIED` limits, and no certification claim.
