# Privacy Audit — Deep Checklist

Loaded on-demand by `SKILL.md`. Covers **GDPR**, **CCPA / CPRA**, **ePrivacy Directive**, with notes for **PIPL** (China), **LGPD** (Brazil), **PIPEDA** (Canada), and **UK GDPR**.

---

## 1. Cookie & Tracker Consent

| ID | Check | Severity if fail | Law |
|----|-------|------------------|-----|
| privacy.cookie.pre-consent-trackers | No analytics/marketing/social trackers fire **before** explicit user consent (EU) | BLOCKER | ePrivacy Art 5(3); GDPR Art 6 |
| privacy.cookie.banner-rejection-equal | "Reject all" is **as prominent and one-click** as "Accept all" | BLOCKER | EDPB 03/2022 + CNIL guidance |
| privacy.cookie.no-pre-checked | No pre-checked consent boxes (incl. legitimate-interest pseudo-opt-in dark patterns) | HIGH | GDPR Art 4(11); Planet49 (CJEU C-673/17) |
| privacy.cookie.granularity | Categories distinguishable (analytics vs marketing vs social vs functional) | HIGH | EDPB 05/2020 |
| privacy.cookie.withdraw-easy | Withdrawing consent is as easy as giving it (footer link or persistent UI) | HIGH | GDPR Art 7(3) |
| privacy.cookie.no-cookie-walls | No "consent or pay" without genuine alternative (region-dependent — EDPB 04/2024 nuance) | HIGH | EDPB 04/2024 |
| privacy.cookie.essential-only-baseline | Strictly necessary cookies set without consent are limited to those required for the service | MEDIUM | ePrivacy Art 5(3) exemption |
| privacy.cookie.documentation | Cookie policy lists every cookie, purpose, third party, retention | MEDIUM | GDPR Art 13 |
| privacy.tracker.fingerprint | Fingerprinting (canvas, font, audio) treated as a tracker requiring consent | HIGH | EDPB 9/2014 + ePrivacy |

### Verification (when browser available)
1. Load page in clean profile.
2. Capture all network requests + `Set-Cookie` headers **before** clicking anything.
3. Any third-party tracker/marketing cookie set pre-consent → `BLOCKER`.
4. Click "Reject all" → re-capture; any non-essential tracker fired → `BLOCKER`.

---

## 2. Privacy Policy Completeness

GDPR Art 13/14 minimum:

- [ ] Identity & contact of controller
- [ ] DPO contact (if appointed; required if Art 37)
- [ ] Purposes of processing **and** lawful basis for each (Art 6)
- [ ] Legitimate-interest balancing summary (when basis = LI)
- [ ] Recipients / categories of recipients
- [ ] International transfers + safeguards (SCCs, adequacy decision, BCRs)
- [ ] Retention period or criteria
- [ ] Data subject rights enumerated + how to exercise
- [ ] Right to lodge complaint with supervisory authority
- [ ] Whether provision is statutory/contractual + consequences of refusal
- [ ] Existence of automated decision-making / profiling + meaningful info about logic
- [ ] Source of data (when not from data subject) per Art 14
- [ ] Last-updated date + change-log practice

CCPA / CPRA additions:

- [ ] Categories of PI collected (CCPA categories)
- [ ] Sources of PI
- [ ] Business / commercial purposes
- [ ] Categories of third parties to whom PI is disclosed/sold/shared
- [ ] Sensitive PI handling disclosure
- [ ] Right to know / delete / correct / opt-out of sale-or-share / limit use of sensitive PI
- [ ] "Do Not Sell or Share My Personal Information" + "Limit the Use of My Sensitive Personal Information" links in footer
- [ ] Notice at collection (may be linked from collection point)

---

## 3. Data Subject Rights (DSR)

| Right | EU (GDPR) | US (CCPA / CPRA) | Verification |
|-------|-----------|-------------------|--------------|
| Access | Art 15 | "Right to know" | Discoverable mechanism, response within 30/45 days, identity verification proportionate |
| Erasure | Art 17 | "Right to delete" | Working flow; cascades to processors; exceptions documented |
| Rectification | Art 16 | "Right to correct" | Mechanism exists; updates propagate |
| Portability | Art 20 | (limited) | Machine-readable export (CSV/JSON) |
| Object | Art 21 | — | Honored, esp. for direct marketing (must always succeed) |
| Restrict | Art 18 | — | Mechanism exists |
| Opt-out of sale/share | — | CCPA "DNS/DNS-S" | Footer link present, GPC respected (CPRA) |
| Limit sensitive PI | — | CPRA | Mechanism exists |
| Automated decision rights | Art 22 | (state-by-state) | Human review path documented |

**Verification:** identify a DSR submission flow (email, form, in-product). Submit a synthetic request if user authorizes; otherwise inspect source for handler and SLA.

---

## 4. Lawful Basis & Consent Engineering

- [ ] Lawful basis recorded per processing activity (Record of Processing — Art 30)
- [ ] Consent (when used) is freely given, specific, informed, unambiguous (Art 4(11))
- [ ] Separate consent for separate purposes (analytics vs marketing vs profiling)
- [ ] Children's data — age gate or parental consent flow if minors plausible (GDPR Art 8: 13–16 depending on member state; COPPA: under 13 in US)
- [ ] Special categories (Art 9) — explicit consent or other Art 9 basis documented (health, biometric, religion, etc.)

---

## 5. Cross-Border Transfers

- [ ] Transfers to "third countries" identified
- [ ] Mechanism per transfer: adequacy decision / SCCs / BCRs / Art 49 derogation
- [ ] Transfer Impact Assessment (TIA) on file when SCCs used (post-Schrems II)
- [ ] EU-US Data Privacy Framework (DPF) — used? Vendor self-certified?
- [ ] Sub-processor list published or available; flow-down clauses in DPAs

---

## 6. Vendor & Processor Management

- [ ] DPA signed with every processor (Art 28)
- [ ] Sub-processor list published or notified
- [ ] Vendor risk assessed (security, location, legal regime)
- [ ] Processor contact for breach notification documented

---

## 7. Breach Response

- [ ] Documented incident response procedure
- [ ] 72-hour notification to supervisory authority capability (Art 33)
- [ ] Data subject notification capability when high risk (Art 34)
- [ ] Breach register maintained

---

## 8. DPIA Triggers (Art 35)

DPIA required when processing is "likely to result in a high risk", including:

- Systematic and extensive profiling with significant effects
- Large-scale processing of Art 9 (special category) or Art 10 (criminal) data
- Systematic monitoring of public areas
- Plus member-state DPA "blacklist" / "whitelist" criteria

If any apply → check if DPIA exists, is documented, and has been updated.

---

## 9. Children & Sensitive Categories

- [ ] If under-13 / under-16 plausible: COPPA / GDPR Art 8 compliance
- [ ] Verifiable parental consent mechanism
- [ ] Reduced data collection from minors
- [ ] No behavioral advertising to minors (CPRA + DSA Art 28 for VLOPs)
- [ ] Art 9 sensitive data: explicit purpose limitation

---

## 10. Documentation & Governance

- [ ] Record of Processing Activities (RoPA) maintained — Art 30
- [ ] Privacy by Design / Default evidence — Art 25
- [ ] DPO appointed when Art 37 applies (public authority / large-scale monitoring / Art 9 large-scale)
- [ ] EU Representative appointed if Art 27 applies (no establishment in EU)
- [ ] Data classification scheme (PII / sensitive / public) applied to actual data stores
- [ ] Retention policies enforced (not just documented)

---

## Quick "go-live" gate (any FAIL = BLOCKER)

1. No tracker fires before consent in EU.
2. Reject-all is one click and equally prominent.
3. Privacy policy exists and lists every Art 13 element.
4. CCPA opt-out link in footer (if US users).
5. Working DSR mechanism published.
6. DPA signed with every third-party processor handling PII.
