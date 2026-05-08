# AI & Content Audit — Deep Checklist

Loaded on-demand by `SKILL.md`. Covers **EU AI Act** (phased applicability), **Copyright Directive** (EU TDM), **DMCA** (US), **CDA Section 230** boundaries, **state AI disclosure laws** (CA AB 2013/SB 942, CO SB 21-169, NYC Local Law 144, etc.).

---

## 1. EU AI Act Risk Classification

The AI Act sorts AI systems into four tiers. Identify each AI system in scope and classify it.

| Tier | Examples | Status |
|------|----------|--------|
| **Unacceptable risk** (Art 5) | Social scoring, real-time biometric ID in public (with narrow LE exceptions), predictive policing of individuals, emotion recognition in workplace/education, untargeted face-image scraping | PROHIBITED — applicable from 2025-02-02 |
| **High risk** (Art 6 + Annex III) | Recruitment/HR, credit scoring, education access, critical infrastructure, law enforcement, migration, judicial use | Strict obligations from 2026-08-02 (Annex III) / 2027-08-02 (some Annex I products) |
| **Limited risk** (Art 50) | Chatbots, AI-generated synthetic content, emotion/biometric categorization | Transparency obligations from 2026-08-02 |
| **Minimal risk** | Spam filters, recommendation widgets, generic ML internals | No specific obligations |
| **GPAI** (Art 51–55) | Foundation models (LLMs, image, audio) | Provider obligations from 2025-08-02 (existing) / 2027-08-02 (older deployed) |

**Provider vs Deployer:** Many obligations differ. If you build the AI system or substantially modify it, you're likely a *provider*. If you only use it, you're a *deployer*.

### Key checks per tier

#### Limited risk (most common for web apps)
- [ ] Users informed they are interacting with an AI system (Art 50(1)) — visible disclosure in chatbot UI
- [ ] AI-generated synthetic image / audio / video / text **labeled as artificially generated** (Art 50(2))
- [ ] Deepfakes labeled (Art 50(4))
- [ ] Emotion-recognition / biometric-categorization users informed (Art 50(3))
- [ ] Disclosures **clearly perceivable** at first interaction, in accessible format

#### High risk (when applicable)
- [ ] Risk management system (Art 9)
- [ ] Data governance + quality (Art 10) — bias, representativeness, no Art 9 sensitive data unless documented basis
- [ ] Technical documentation (Art 11 + Annex IV)
- [ ] Logging / record-keeping (Art 12)
- [ ] Transparency to deployers (Art 13) — instructions for use
- [ ] Human oversight (Art 14)
- [ ] Accuracy, robustness, cybersecurity (Art 15)
- [ ] Quality management system (Art 17)
- [ ] Conformity assessment + EU declaration of conformity + CE marking (Art 43, 47, 48)
- [ ] Registration in EU database (Art 49)
- [ ] Post-market monitoring (Art 72)
- [ ] Incident reporting (Art 73)

#### GPAI provider
- [ ] Technical documentation (Art 53) — at least Annex XI
- [ ] Information for downstream providers (Art 53) — Annex XII
- [ ] Copyright policy + EU TDM opt-out respected (Art 53(1)(c))
- [ ] **Public summary of training data** (Art 53(1)(d)) — using Commission template
- [ ] If "systemic risk" GPAI (Art 51 thresholds): model evaluation, adversarial testing, incident tracking, cybersecurity (Art 55)

---

## 2. Copyright & Training Data

### EU Copyright Directive (Directive 2019/790)
- [ ] **Art 4 TDM exception:** respected when right-holders haven't opted out via machine-readable means (e.g., `robots.txt` / `ai.txt` / metadata)
- [ ] **Art 3 TDM:** for research orgs, no opt-out — but commercial use should rely on Art 4
- [ ] If using third-party model: provider's training-data policy reviewed for opt-out compliance
- [ ] Site itself sets opt-out signals if it doesn't want its content used for training (e.g., `User-agent: GPTBot Disallow: /`)

### US (no statutory TDM exception — fair use case-by-case)
- [ ] Track guidance from active litigation (Authors v. OpenAI, NYT v. Microsoft, etc.)
- [ ] License training data when feasible
- [ ] Attribution / provenance metadata preserved when generated content reuses identifiable inputs

### Outputs
- [ ] AI-generated content reviewed for substantial similarity to training inputs
- [ ] Where outputs may include identifiable third-party content (e.g., code, lyrics), terms of service flag this risk to users
- [ ] User-generated content uploaded to your service: license terms permit your AI uses (or explicit opt-in)

---

## 3. DMCA Compliance (US, for hosting / UGC platforms)

§512 safe-harbor preconditions:
- [ ] **Designated DMCA agent registered** with US Copyright Office (renewed every 3 years)
- [ ] Agent contact published on the site (typically `/dmca` or `/copyright`)
- [ ] **Takedown procedure** documented + functioning
- [ ] Acknowledge & act on valid takedown notices "expeditiously"
- [ ] **Counter-notice** procedure documented
- [ ] **Repeat-infringer policy** documented and enforced
- [ ] No interference with standard technical measures

### EU mirror — Copyright Directive Art 17 (online content-sharing service providers)
- [ ] Best-efforts to obtain authorization for protected content
- [ ] Best-efforts to ensure unavailability of unauthorized content (notice + stay-down)
- [ ] Complaint & redress mechanism

---

## 4. State AI Disclosure Laws (US)

### California
- [ ] **AB 2013 (effective 2026-01-01):** GenAI training-data documentation published if model offered/modified in CA
- [ ] **SB 942 (CA AI Transparency Act):** GenAI providers (>1M monthly visitors) must offer free AI-detection tool + watermark/manifest options
- [ ] **AB 1008:** PI under CCPA includes AI-generated info derived from PI
- [ ] **SB 1001 (Bot disclosure):** disclose bot identity in commerce/election contexts
- [ ] **AB 2655 (Defending Democracy):** election deepfake provisions

### Colorado
- [ ] **SB 21-169 (Insurance):** no algorithmic discrimination in insurance
- [ ] **CO AI Act (SB 24-205, effective 2026-02-01):** high-risk AI duty of care, impact assessments, consumer notification (developer + deployer obligations)

### Illinois
- [ ] **AI Video Interview Act:** consent + disclosure if AI used in hiring video interviews
- [ ] **HB 3773 (effective 2026-01-01):** civil rights protections in AI employment decisions

### NYC
- [ ] **Local Law 144 (AEDT):** annual independent bias audit for automated employment decision tools; candidate notice

### Federal
- [ ] **FTC Section 5:** no deceptive claims about AI capability or training; no unfair AI-driven harms
- [ ] **EEOC + DOJ joint guidance** on AI in employment

---

## 5. AI in User-Affecting Decisions

If AI materially affects employment, credit, insurance, housing, education access, healthcare, or legal:

- [ ] Notify affected user of AI use (timing varies by law)
- [ ] Provide explanation of factors / "meaningful information about the logic" (GDPR Art 22; CO AI Act; CCPA limited)
- [ ] Right to human review / appeal
- [ ] Document model card, validation, fairness testing
- [ ] Avoid Art 22 GDPR solely-automated decision unless one of three legal bases met

---

## 6. Watermarking & Provenance

- [ ] Synthetic-media labeling implemented (AI Act Art 50(2))
- [ ] C2PA / Content Credentials embedded where supported (recommended)
- [ ] Watermarks tested for robustness against trivial removal
- [ ] CA SB 942 detection tool + manifest (when applicable)

---

## 7. Bot & Chatbot Disclosure

- [ ] Chatbot identifies as AI on first interaction (AI Act Art 50; CA SB 1001)
- [ ] Hand-off to human option offered for sensitive interactions (where required)
- [ ] System prompt / persona doesn't claim human identity in deceptive way

---

## 8. Section 230 / Liability Boundaries (US)

- [ ] Platform doesn't materially contribute to creation of unlawful content (would erode 230 immunity)
- [ ] AI-generated outputs by the platform itself: 230 likely *does not* protect (per emerging case law) → moderate
- [ ] Recommender systems: defend with 230(c)(1) where possible; document content-neutral signals

---

## 9. Transparency Reports (DSA + voluntary)

If DSA hosting / online platform:
- [ ] AI-driven moderation disclosed (volume, accuracy, error rates) per Art 15 / Art 24

Voluntary best practice:
- [ ] Annual AI transparency report (model versions, deprecations, incidents, demographic performance)

---

## Quick "go-live" gate (any FAIL = BLOCKER if AI features are user-facing in scope)

1. Chatbot / AI assistant: clear disclosure that it's AI (Art 50).
2. AI-generated synthetic media: labeled (Art 50(2)).
3. UGC platform (US): DMCA agent registered, takedown flow live.
4. UGC platform (EU): notice & action mechanism live.
5. GPAI provider: training-data summary published (Art 53(1)(d)).
6. AI in employment/credit/insurance: notice + explanation + human review path.
7. No prohibited Art 5 use cases active.
