# Regulatory Guard — Example Run

This is a condensed example of a real-world audit output. Use it as a template for the report shape.

## Target

- **Site:** https://example-shop.eu
- **Source:** ./apps/web (Next.js 15, deployed on Vercel)
- **Business:** Direct-to-consumer apparel, ships globally
- **Audit date:** 2026-05-08

## Applicability Matrix

| Law | Applies | Reason |
|-----|---------|--------|
| GDPR + ePrivacy | YES | EU customers; analytics + marketing trackers; account creation |
| CCPA / CPRA | YES | Ships to California; "California" mentioned in shipping page |
| EAA (from 2025-06-28) | YES | B2C e-commerce in EU |
| WCAG 2.2 AA | YES | Bar for both EAA and ADA |
| ADA Title III | YES | US customers, place of public accommodation per DOJ |
| CRD + Omnibus + UCPD | YES | EU consumer e-commerce |
| DSA | LIMITED | Online platform Art 6, but micro-enterprise carve-out may apply — confirm headcount + turnover |
| DMA | NO | Not a designated gatekeeper |
| EU AI Act | LIMITED | "Style assistant" chatbot = limited-risk Art 50 transparency |
| DMCA | NO | No third-party UGC at meaningful scale |
| CAN-SPAM | YES | US marketing emails |

## Summary

| Severity | Count |
|----------|-------|
| BLOCKER  | 4 |
| HIGH     | 9 |
| MEDIUM   | 14 |
| LOW      | 6 |
| UNVERIFIED | 3 |
| PASS     | 38 |

**Verdict:** **NOT READY** — 4 blockers must be resolved before next public deploy.

---

## Findings — Privacy

```
[privacy.cookie.pre-consent-trackers]
  severity: BLOCKER
  evidence:
    - URL: https://example-shop.eu/
    - request: GET https://www.googletagmanager.com/gtag/js?id=G-XXXX (fired before banner interaction)
    - request: POST https://stats.g.doubleclick.net/j/collect (fired before banner)
    - source: apps/web/app/layout.tsx:23 — <Script src="..." strategy="afterInteractive" />
    - cookie: _ga=GA1.2.123456789... (Set on landing pre-consent)
  applicable_law: GDPR Art 6 + ePrivacy Art 5(3); EDPB 03/2022
  remediation:
    - Remove eager <Script> insertion
    - Use a consent-aware loader (e.g., Cookiebot / OneTrust / custom hook gated on consent state)
    - Default state = no non-essential cookies
  effort: S (1–2 days)
```

```
[privacy.cookie.banner-rejection-equal]
  severity: BLOCKER
  evidence:
    - URL: https://example-shop.eu/
    - screenshot: Accept = solid green button; Reject = small underlined text link in corner
  applicable_law: ePrivacy Art 5(3); EDPB 03/2022; CNIL guidance
  remediation:
    - Reject-all button visually equivalent to Accept-all (size, contrast, position)
    - Both reachable in single click, no nested menu for "reject"
  effort: XS
```

```
[privacy.dsr.no-mechanism]
  severity: BLOCKER
  evidence:
    - URL: https://example-shop.eu/privacy — mentions rights but no contact/form
    - search: no `/privacy/request` or DSAR endpoint found in source
  applicable_law: GDPR Art 12, 15–22; CCPA §1798.130
  remediation:
    - Add /privacy/request page with form (data type + identity verification + email confirmation)
    - Document SLA in privacy policy (30 days GDPR / 45 days CCPA)
  effort: M
```

```
[privacy.policy.missing-retention]
  severity: HIGH
  evidence:
    - URL: https://example-shop.eu/privacy — no retention period or criteria for any data category
  applicable_law: GDPR Art 13(2)(a)
  remediation:
    - Add retention table per data category
  effort: S
```

(... 6 more privacy findings omitted ...)

---

## Findings — Accessibility

```
[a11y.2.1.1.keyboard-trap-modal]
  severity: BLOCKER
  evidence:
    - URL: https://example-shop.eu/cart (modal opens on Add to Cart)
    - manual: Tab cycles inside modal correctly, but no key returns focus to trigger; Escape doesn't close
  applicable_law: WCAG 2.1.2; EAA / EN 301 549 §9.2.1.2
  remediation:
    - Implement focus trap with restoration to trigger on close
    - Add Escape handler
    - Use a battle-tested primitive (Radix Dialog, Headless UI Dialog, native <dialog>)
  effort: S
```

```
[a11y.1.4.3.contrast-cta]
  severity: HIGH
  evidence:
    - URL: https://example-shop.eu/products/shirt-001
    - measurement: "Add to Cart" button #FFB300 on #FFFFFF = 1.94:1 (needs ≥4.5:1)
  applicable_law: WCAG 1.4.3
  remediation:
    - Darken button background to #B58300 (4.74:1) or change text to dark
  effort: XS
```

(... 5 more accessibility findings omitted ...)

---

## Findings — Consumer & E-commerce

```
[consumer.pricing.fees-at-checkout]
  severity: BLOCKER
  evidence:
    - URL: https://example-shop.eu/cart → /checkout
    - observation: "€4.50 service fee" appears only on final page
  applicable_law: CRD Art 6(1)(e); UCPD; CA SB 478
  remediation:
    - Disclose unavoidable fees in product or cart page, before review
  effort: S
```

(... more findings omitted ...)

---

## Findings — AI & Content

```
[ai.chatbot.disclosure-missing]
  severity: HIGH
  evidence:
    - URL: https://example-shop.eu/ — chat widget bottom-right
    - observation: no "AI assistant" label; persona "Sophie" suggests human
  applicable_law: EU AI Act Art 50(1); CA SB 1001 (commerce)
  remediation:
    - Label widget "AI Assistant"
    - First message: "Hi, I'm an AI assistant. Type 'human' to reach a person."
  effort: XS
```

(... more findings omitted ...)

---

## Remediation Plan (BLOCKER + HIGH)

| ID | Severity | Owner | Effort | Description |
|----|----------|-------|--------|-------------|
| privacy.cookie.pre-consent-trackers | BLOCKER | eng | S | Gate trackers behind consent state |
| privacy.cookie.banner-rejection-equal | BLOCKER | design + eng | XS | Equal-prominence reject-all |
| privacy.dsr.no-mechanism | BLOCKER | eng + legal | M | DSAR form + workflow |
| consumer.pricing.fees-at-checkout | BLOCKER | eng | S | Show service fee in cart |
| a11y.2.1.1.keyboard-trap-modal | BLOCKER | eng | S | Replace modal with accessible primitive |
| privacy.policy.missing-retention | HIGH | legal | S | Update retention disclosure |
| a11y.1.4.3.contrast-cta | HIGH | design | XS | Adjust button contrast |
| ai.chatbot.disclosure-missing | HIGH | eng | XS | AI label + first-message disclosure |
| ... | ... | ... | ... | ... |

## Out of Scope / Unverified

- `privacy.policy.subprocessor-list`: page links to a PDF that returned 403 — please re-share
- `consumer.refund.flow`: requires authenticated session; rerun with synthetic test account
- `ai.training-data`: model is a third-party API (Claude); confirm provider's TDM-opt-out policy is referenced in your terms

## Limitations

This audit is a structured technical review, not legal advice. High-severity findings should be reviewed by qualified counsel for the relevant jurisdictions.
