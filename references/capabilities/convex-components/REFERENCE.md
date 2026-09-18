## Contract

- Input: Consumer rules, installed Convex version, component/host scope, exports, schema, generated API, codegen and test scripts.
- Output: Reusable component, boundary and authorization evidence, public-path tests, consumer integration evidence, and deployment-dependent gaps.
- Effects: Authorized component changes and tests. It does not deploy merely to validate.

### Acceptance

- Component and host ownership, API, lifecycle, and authorization boundaries are explicit.
- Public and cross-tenant failure paths have observed test evidence.
- A packed consumer resolves, mounts, generates, and exercises the public API.
- Compilation and codegen remain distinct from observed consumer integration.

## Procedure

1. Define consumers, component-owned state/lifecycle, host-owned identity/domain data, public operations, failures, retention, pagination, tenant scope, and installed API assumptions. Reuse an official component when it fits.
2. Keep schema, functions, generated files, and schedules inside the component boundary. Host and siblings use generated references and `ctx.runQuery`, `ctx.runMutation`, or `ctx.runAction`; never hand-edit generated files.
3. Validate exported arguments and returns at runtime. Keep queries read-only, mutations transactional, and external effects in actions; bound batches and make retries and partial external failure recoverable.
4. Require the host to authenticate, derive trusted scope, and authorize before calls. Keep host secrets, schemas, and privileged wrappers outside the component.
5. Test public paths, validator failures, identity and tenant denial, two instances, retries, pagination, schedules, external failure, consumer mounting, type generation, packaging, and affected documentation/migration checks.
6. Return material boundary, authorization, or recovery uncertainties and current evidence to the caller's quality validation. When standalone, return deployment-dependent gaps with the next verification. After an authorized repair, prove isolated failure then success and rerun invalidated component and consumer checks.

## Pitfalls

- Caller-provided scope is not membership proof; the host must derive trusted scope before authorizing.
- Type generation does not prove consumer behavior; mount and exercise the packed public API.
