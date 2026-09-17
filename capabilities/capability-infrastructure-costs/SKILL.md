---
name: capability-infrastructure-costs
description: Model current and projected infrastructure costs from observed usage and verified pricing, compare equivalent options, and expose assumptions, uncertainty, and missing evidence without changing services.
---

## Contract

- Input: Authorized usage and billing evidence, provider metadata, decision owner/date, environments, billing period, forecast horizon, currency, and requirements.
- Output: Auditable baseline and scenarios, reconciled totals, decision-changing inputs, uncertainty, and conditional recommendation.
- Effects: Read-only cost modeling. It does not provision, resize, purchase, cancel, change billing, or generate paid workloads.

### Acceptance

- Decision owner/date, dated sources, observed inputs, assumptions, allocations, exclusions, currency, and confidence are recorded.
- Baseline and scenarios meet comparable capacity and recovery requirements.
- Totals reconcile available evidence and expose inputs that change the decision.
- The recommendation states uncertainty and any conditional savings.

## Procedure

1. Set the decision owner, date, environments, billing period, forecast horizon, currency, and performance, availability, privacy, and recovery requirements. Separate infeasible options.
2. Inventory billable and shared resources from configuration, authorized exports, and provider metadata. Reconcile coverage, pages, credits, exclusions, account visibility, and missing usage without exposing sensitive payloads.
3. Retrieve dated contractual, invoice, or official prices. Match region, tier, units, commitments, quotas, overages, minimums, taxes, and currency conversion source/date/rate; distinguish billed values from list prices.
4. Model baseline quantities, conversions, tiers, fixed/one-time costs, compute, storage/backups, transfer, managed services, CI, and shared allocation once under an explicit rule.
5. Model low/expected/high scenarios from measured drivers or labeled assumptions, including thresholds, redundancy, recovery, operations labor, migration, and commitments. Show sensitivities and uncertainty.
6. Reconcile arithmetic, units, tier boundaries, allocations, and totals with available invoices or exports. Return material uncertainty and current evidence to the caller's quality validation. When standalone, return the next discriminating input; rerun affected calculations after changed sources or authorized model repair.

## Pitfalls

- Missing usage or price data is not zero cost; model it as an exclusion or conditional assumption.
- List prices are not invoices; identify their source and do not present them as billed values.
