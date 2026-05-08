# Consumer & E-commerce Audit — Deep Checklist

Loaded on-demand by `SKILL.md`. Covers **Digital Services Act (DSA)**, **Digital Markets Act (DMA)**, **Consumer Rights Directive (CRD)**, **Omnibus Directive**, **Unfair Commercial Practices Directive (UCPD)**, **CCPA / CPRA "sale or share"**, **CAN-SPAM** (US), **CASL** (Canada), and emerging **dark-pattern** rules.

---

## 1. Pricing Transparency

### EU (CRD + Omnibus + UCPD)
- [ ] **Total price** including taxes shown before order placement (CRD Art 6(1)(e))
- [ ] **Unit price** displayed where applicable (Price Indication Directive)
- [ ] Delivery / additional charges disclosed before checkout (CRD Art 6(1)(e))
- [ ] No drip pricing — all unavoidable fees shown upfront (UCPD)
- [ ] Currency unambiguous, conversion rates disclosed if shown
- [ ] **Discount reference price** = lowest price in last 30 days (Omnibus Art 2 / CRD Art 6a)
- [ ] Personalized pricing disclosed when used (Omnibus)

### US (FTC + state laws)
- [ ] No hidden / "junk" fees (FTC Junk Fees Rule, effective 2025-05-12: total price upfront for live-event tickets and short-term lodging; broader proposed rules)
- [ ] California SB 478 — "honest pricing" (in effect 2024-07-01): no fees added beyond posted price for goods/services to consumers

---

## 2. Withdrawal / Refund / Cancellation

### EU (CRD)
- [ ] 14-day right of withdrawal stated for distance-sold goods/services (Art 9)
- [ ] Standard withdrawal form provided (Annex I)
- [ ] Pre-contract info (Art 6) provided in durable medium
- [ ] Order confirmation in durable medium (email or download)
- [ ] Withdrawal effects: refund within 14 days, including original delivery (Art 13)
- [ ] Exceptions documented (digital content with consent, sealed goods, perishables)

### US (state-by-state)
- [ ] FTC Cooling-Off Rule for door-to-door / off-premises sales >$25/$130
- [ ] California "automatic renewal" law: clear terms + cancellation method as easy as signup
- [ ] **FTC Click-to-Cancel Rule** (when in force) — cancellation method must be at least as simple as the sign-up method
- [ ] Negative-option opt-in clarity (no pre-checked boxes)

---

## 3. Reviews, Rankings & Endorsements (Omnibus + FTC)

### EU
- [ ] Discloses whether and how reviews are verified to come from real users
- [ ] Discloses ranking parameters and their relative weight (CRD Art 6a, Platform-to-Business Reg)
- [ ] No fake reviews (paid or AI-generated unverified)

### US (FTC Endorsement Guides + 16 CFR Part 465 — Fake Reviews Rule, 2024)
- [ ] No fake or AI-generated reviews of own product
- [ ] Material connections disclosed for endorsements/affiliates
- [ ] No suppressing negative reviews
- [ ] No buying/selling fake social indicators

---

## 4. Dark Patterns & Manipulative Design

Based on EDPB 03/2022, OECD, FTC, CPRA:

| Pattern | Why illegal/risky |
|---------|-------------------|
| Asymmetric choice (Accept big, Reject hidden) | DSA Art 25; CPRA; UCPD |
| Confirmshaming ("No thanks, I hate saving money") | UCPD; CPRA |
| Roach motel (easy in, hard out) | FTC Click-to-Cancel; CPRA |
| Forced action / forced registration | UCPD |
| Misdirection (urgency/scarcity untrue) | UCPD; FTC |
| Visual interference (greyed-out reject button) | EDPB; CPRA |
| Trick wording (double negatives, ambiguous defaults) | UCPD; CPRA |
| Pre-selected options that incur charges (CRD Art 22) | CRD; UCPD |

**DSA Art 25:** "Online platforms shall not design, organise or operate their online interfaces in a way that deceives, manipulates or otherwise materially distorts" user choices.

---

## 5. DSA — Digital Services Act

Applies to **intermediary services**: mere conduit, caching, **hosting** (incl. online platforms, search). Tiered obligations.

### All hosting / online platforms
- [ ] Notice & action mechanism (Art 16) — easy reporting of illegal content
- [ ] Statement of reasons for content moderation actions (Art 17) — sent to user + DSA Transparency DB
- [ ] Trusted flagger priority (Art 22) — when designated
- [ ] No dark patterns (Art 25)
- [ ] Online advertising transparency (Art 26) — labeled "advertisement" + parameters
- [ ] No targeted ads to minors (Art 28)
- [ ] No targeted ads using sensitive data (Art 26(3))
- [ ] Recommender system parameters disclosed (Art 27)
- [ ] Online interfaces accessible for minors when service used by them (Art 28)

### Online platforms (excl. micro/small)
- [ ] Internal complaint-handling system (Art 20)
- [ ] Out-of-court dispute settlement option (Art 21)
- [ ] Trader traceability for B2C marketplaces (Art 30 — "Know Your Business Customer")
- [ ] Annual transparency report (Art 24)

### VLOPs / VLOSEs (>45M EU MAU)
- [ ] Annual systemic risk assessment (Art 34)
- [ ] Risk mitigation measures (Art 35)
- [ ] Independent audit (Art 37)
- [ ] At least one non-profiling-based recommender option (Art 38)
- [ ] Ad repository (Art 39)
- [ ] Data access for researchers (Art 40)
- [ ] Compliance officer (Art 41)

---

## 6. DMA — Digital Markets Act

Only applies to **designated gatekeepers** (Commission decision). If not designated → SKIP.

If designated, core platform service obligations (Art 5–7):
- [ ] Interoperability for messaging (Art 7)
- [ ] No self-preferencing in ranking (Art 6(5))
- [ ] No combining personal data across services without explicit consent (Art 5(2))
- [ ] Allow third-party app stores / sideloading (Art 6(4))
- [ ] Allow business users to communicate offers outside the platform (Art 5(4))
- [ ] Real-time data portability for end users (Art 6(9))

---

## 7. Marketing Communications

### Email (US — CAN-SPAM)
- [ ] Accurate "From" / "Reply-To" / routing info
- [ ] Subject line not deceptive
- [ ] Identified as ad (when applicable)
- [ ] Valid physical postal address in every email
- [ ] Working unsubscribe in every email; honored within 10 business days
- [ ] No further mail to that address after unsubscribe (except transactional)

### Email (EU — ePrivacy Art 13 + GDPR)
- [ ] Prior opt-in consent for marketing (or soft opt-in for existing-customer's similar products with each email having unsubscribe)
- [ ] Unsubscribe in every email; honored immediately
- [ ] Sender identity clear, no concealing
- [ ] Granular consent: marketing ≠ analytics ≠ profiling

### Email (Canada — CASL)
- [ ] Express or implied consent on file (timestamped)
- [ ] Sender ID + contact info in every email
- [ ] Unsubscribe processed within 10 business days

### SMS / Push
- [ ] Prior express consent (TCPA in US for marketing SMS)
- [ ] STOP keyword honored (US)
- [ ] Quiet hours respected

---

## 8. Cookie / Consent Reuse

- [ ] Marketing consent **separate** from analytics consent
- [ ] Profiling consent **separate** from marketing
- [ ] Consent receipt logged (timestamp, version, choices) for audit

---

## 9. Subscription & Auto-Renewal

- [ ] Auto-renewal disclosed in pre-contract info
- [ ] Renewal reminder before charge (varies by jurisdiction; required in CA, NY, IL, OR, etc.)
- [ ] Cancellation flow as easy as sign-up (FTC Click-to-Cancel; CRD)
- [ ] Free trial → paid: no automatic conversion without re-consent in some jurisdictions
- [ ] Price changes: prior notice + opt-out

---

## 10. Children & Vulnerable Consumers

- [ ] Age gate where service not intended for under-13/16
- [ ] Reduced data + no behavioral ads to minors (DSA Art 28; CPRA; COPPA)
- [ ] No exploitative dark patterns targeting cognitive limits
- [ ] Clear, age-appropriate language where minors permitted

---

## 11. Marketplace / UGC Specific

- [ ] B2C trader vs C2C seller clearly identified to consumer (CRD Art 6a; Omnibus)
- [ ] If platform is the trader: full CRD obligations
- [ ] If platform is intermediary: clear party identification + dispute path
- [ ] Trader traceability per DSA Art 30

---

## Quick "go-live" gate (any FAIL = BLOCKER for the relevant jurisdiction)

1. Total price (incl. taxes/unavoidable fees) shown before checkout.
2. 14-day withdrawal right disclosed for EU consumers.
3. Working unsubscribe in every marketing email + accurate sender info.
4. Reject-all consent path is one click and equally prominent (cross-ref privacy.md).
5. CCPA "Do Not Sell or Share" link in footer (US users + sale/share).
6. Cancellation flow at least as easy as sign-up.
7. No DSA Art 25 dark patterns in critical flows (consent, checkout, account deletion).
