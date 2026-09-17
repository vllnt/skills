---
name: capability-infrastructure-review
description: Assess infrastructure exposure, access, isolation, dependencies, and recovery from current evidence; return prioritized findings and verification gaps without changing infrastructure.
---

# Capability Infrastructure Review

Assess infrastructure posture and resilience without changing infrastructure, permissions, deployments, or data. Discover providers, environments, service owners, requirements, and permitted reads from consumer instructions and configuration.

## Procedure

1. Set the question, authorized scope, environment identities, and required availability, isolation, and recovery outcomes. Resolve ambiguous production targets before querying them.
2. Inventory configuration and authorized control-plane metadata; exhaust relevant pagination and reconcile declared and observed resources, owners, revisions, drift, truncation, and inaccessible sources.
3. Map entry points, trust boundaries, identities, privileged paths, DNS/network exposure, secret handling, tenant separation, and shared dependencies. Use redacted metadata only; do not retrieve or retain secret values.
4. Assess applicable least privilege, public/private reachability, encryption, resource isolation, failure domains, redundancy, health signals, and operational ownership against actual requirements.
5. Check backup scope, retention, restore evidence, recovery targets, and dependency failure handling. Configuration and green health do not prove restore, recovery, or runtime isolation; active scans, fault injection, restore exercises, and changes need separate authority.
6. Return a dated topology and coverage ledger that another assessment can reuse, plus prioritized findings with resource/environment, observation time, requirement, evidence, impact, confidence, remedy, dependencies, and verification/recovery. For material unresolved questions, use independent review and critique when available; otherwise assess sequentially; for changed evidence or an authorized repair, reassess affected controls. Otherwise report exact blocked checks and unverified controls.

## Definition of Done

- Coverage records observed environments/resources and inaccessible, stale, or truncated evidence.
- Findings connect requirements to current evidence, impact, remediation, and verification/recovery.
- Exposure, access, isolation, backup, and recovery are assessed where applicable.
- The conclusion states assessed posture, unverified controls, and remaining verification/recovery work.
