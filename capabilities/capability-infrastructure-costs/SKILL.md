---
name: capability-infrastructure-costs
description: Model current and projected infrastructure costs from observed usage and verified pricing, compare equivalent options, and expose assumptions, uncertainty, and missing evidence without changing services.
---

# Capability Infrastructure Costs

Build an auditable cost model without provisioning, resizing, purchasing, cancelling, changing billing, or generating paid workloads. Discover providers, services, currencies, budgets, and business units from authorized evidence.

## Procedure

1. Set the decision owner, decision date, environments, billing period, forecast horizon, currency, and required performance, availability, privacy, and recovery. Separate infeasible options.
2. Inventory billable and shared resources from configuration, authorized usage/billing exports, and provider metadata. Reuse a current infrastructure inventory when supplied, but reconcile its coverage before modeling. Reconcile pages, credits, exclusions, account visibility, and missing usage without exposing sensitive payloads.
3. Retrieve dated contractual, invoice, or official prices. Match region, tier, units, commitments, quotas, overages, minimums, taxes, and any currency-conversion source, date, and rate; distinguish billed values from list prices.
4. Model baseline quantities, conversions, tiers, fixed/one-time costs, compute, storage/backups, transfer, managed services, CI, and shared allocation once under an explicit rule. Do not treat missing costs as zero.
5. Model low/expected/high scenarios from measured drivers or labeled assumptions, including capacity thresholds, redundancy, recovery, operations labor, migration, and commitments. Show sensitivities and uncertainty.
6. Reconcile arithmetic, units, tier boundaries, allocations, and totals with available invoices or exports. For material unresolved questions, use independent review and critique when available; otherwise assess sequentially; for changed sources or an authorized model repair, rerun affected calculations and sensitivity checks. Blocked evidence yields conditional scenarios and the next discriminating input.

## Definition of Done

- Decision owner/date, dated sources, observed inputs, assumptions, allocations, exclusions, currency, and confidence are recorded.
- Baseline and scenarios meet comparable capacity and recovery requirements.
- Totals reconcile available evidence and expose the inputs that change the decision.
- The recommendation states its uncertainty, decision-changing inputs, and any conditional savings.
