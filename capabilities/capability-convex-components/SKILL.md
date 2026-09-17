---
name: capability-convex-components
description: Design, implement, and test reusable Convex components with isolated state, typed client APIs, host-owned authorization, safe scheduling, and verified consumer integration.
---

# Capability Convex Components

Deliver a reusable component with isolated state and verified public behavior. Inspect consumer rules, installed Convex version, exports, schema, generated API, and codegen/test scripts; do not deploy merely to validate.

## Procedure

1. Define consumers, component-owned state/lifecycle, host-owned identity/domain data, public operations, failures, retention, pagination, tenant scope, and installed API assumptions. Reuse an official component when it already fits.
2. Keep schema, functions, generated files, and schedules inside the component boundary. Host and siblings use generated references and `ctx.runQuery`, `ctx.runMutation`, or `ctx.runAction`; never hand-edit generated files.
3. Validate exported arguments and returns at runtime. Keep queries read-only, mutations transactional, and external effects in actions; bound batches and make retries and partial external failure recoverable.
4. The host authenticates, derives trusted scope, and authorizes before calls. Never trust caller scope as membership, import host secrets/schemas, or expose privileged wrappers.
5. Test public paths, validator failures, identity and tenant denial, two instances, retries, pagination, schedules, external failure, consumer mounting, type generation, packaging, and affected documentation/migration checks.
6. For material boundary, authorization, or recovery questions, use independent review and critique perspectives when available; otherwise apply them sequentially. Reuse caller evidence only when component revision, host, environment, and proof remain current. For an authorized repair, prove isolated failure then success and rerun invalidated component and consumer checks; report deployment-dependent gaps with the next verification.

## Definition of Done

- Component and host ownership, API, lifecycle, and authorization boundaries are explicit.
- Public and cross-tenant failure paths have observed test evidence.
- A packed consumer resolves, mounts, generates, and exercises the public API.
- The result distinguishes compilation/codegen from observed consumer integration.
