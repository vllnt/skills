---
name: capability-infrastructure-review
description: Assess infrastructure exposure, access, isolation, dependencies, and recovery from current evidence; return prioritized findings and verification gaps without changing infrastructure.
---

## Contract

- Input: Consumer instructions, authorized scope, environment identities, configuration, control-plane metadata, and availability, isolation, and recovery requirements.
- Output: Dated topology and coverage ledger, prioritized findings, verification/recovery work, and unverified controls.
- Effects: Read-only infrastructure assessment. It does not change infrastructure, permissions, deployments, or data.

### Acceptance

- Coverage records observed environments/resources and inaccessible, stale, or truncated evidence.
- Findings connect requirements to current evidence, impact, remediation, and verification/recovery.
- Exposure, access, isolation, backup, and recovery are assessed where applicable.
- The conclusion states assessed posture, unverified controls, and remaining work.

## Procedure

1. Set the question, authorized scope, environment identities, and required availability, isolation, and recovery outcomes. Resolve ambiguous production targets before querying them.
2. Inventory configuration and authorized control-plane metadata; exhaust relevant pagination and reconcile declared and observed resources, owners, revisions, drift, truncation, and inaccessible sources.
3. Map entry points, trust boundaries, identities, privileged paths, DNS/network exposure, secret handling, tenant separation, and shared dependencies. Use redacted metadata only; do not retrieve or retain secret values.
4. Assess applicable least privilege, reachability, encryption, resource isolation, failure domains, redundancy, health signals, and operational ownership against actual requirements.
5. Check backup scope, retention, restore evidence, recovery targets, and dependency failure handling. Treat active scans, fault injection, restore exercises, and changes as separately authorized work.
6. Return the topology, coverage ledger, and findings with resource/environment, observation time, requirement, evidence, impact, confidence, remedy, dependencies, and verification/recovery. Return material uncertainty and current evidence to the caller's quality validation. When standalone, return blocked checks; reassess affected controls after changed evidence or authorized repair.

## Pitfalls

- Green health or configuration does not prove restore, recovery, or runtime isolation; require observed proof for those claims.
- Declared resources can differ from observed resources; reconcile both and report inaccessible pages or sources.
