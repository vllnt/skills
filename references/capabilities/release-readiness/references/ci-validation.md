# CI validation

## Inspect effective behavior

Discover the actual CI system, repository commands, tool versions, lockfiles, and release policy. Reuse existing workflows. Search results identify candidates; inspect job conditions, triggers, reusable workflows, dependencies, and command semantics before conclusions. No CI, test, lint, or build command is universally mandatory: assess the repository's requirements and artifact risks.

Required checks must apply to the exact candidate revision and relevant environment. Verify the configured names/identities against executed results. Pending, skipped, neutral, canceled, missing, or allowed-failure jobs do not automatically prove the required behavior. Account for path filters and merge queues; a successful unrelated run is not proof. Respect the host's actual required-check semantics while separately reporting unexercised behavior. Never weaken protections or checks to get green.

## Protection evidence

Where authorized read access exists, inspect branch protection and applicable repository/organization rulesets, including tag rules. Discover the default branch rather than assuming `main`. A 404 may mean missing access, a hidden resource, or an absent legacy protection endpoint; it does not establish that the branch is unprotected. Report uncertainty and continue local inspection. Do not modify settings as part of validation.

## Safe workflow changes

- Prefer repairing existing jobs over adding a parallel CI/release system.
- Use the project's verified commands, supported toolchain, lockfile, and dependency policy. Do not assume a `lint` script, globally installed tool, `latest` download, or OIDC support.
- Pin actions/tool downloads to reviewed versions or immutable revisions according to project policy; verify provenance/checksums where required. Do not execute remote installers merely to inspect a repository.
- Default job tokens to read-only; grant write permissions only to the job and resource that need them. Disable persisted checkout credentials when no push is required.
- Never expose secrets or write tokens to untrusted PR code. Avoid privileged `pull_request_target` execution of a contributor checkout. Keep publishing behind the actual protected release boundary.
- Distinguish static workflow validation from executed evidence. Test success and relevant failure/skip paths in an authorized isolated environment; do not publish merely to validate a template.

## Protected-branch release pattern

This is a design template to adapt, not a turnkey publishing workflow:

1. Prepare version, lockfile, changelog, and generated documentation edits on a release branch using existing repository tooling. Return a local patch if opening a PR is not authorized.
2. Land release preparation through the repository's protected review/merge process and required checks. CI must not commit or push those edits directly to the protected default branch.
3. Resolve the approved merged revision and version. Verify candidate-specific checks and artifact/version agreement before any tag or publication.
4. An authorized release job may create the intended tag at that revision, subject to tag rules; an existing tag must match exactly or the operation stops. Do not move tags or assume they bypass protection.
5. Build from the verified immutable revision and publish through the existing registry/host workflow. Confirm OIDC/trusted-publisher configuration and compatible pinned tooling before using it; otherwise use the repository's approved credential mechanism. Never delete authentication configuration as a generic workaround.
6. Record artifact identity and publication receipts, reobserve the registry/host, and report partial failures. Inspect external state before retries; do not republish blindly.

Use separate permissions by responsibility:

| Responsibility | Typical minimum permission; verify against actual provider |
|---|---|
| Inspect/test/build | `contents: read`; no registry credentials |
| Open release-preparation PR | Only the authorized branch/PR writer needs repository write access |
| Create authorized tag/release | `contents: write` on the gated release job only |
| Registry OIDC publication | `contents: read` plus `id-token: write` on the publisher only, after trusted-publisher setup |

Do not automatically add canary publication or a release workflow to a library. Existing manual or external release processes can be valid. No example should bypass branch protection, upgrade to an unreviewed latest CLI, infer publication authority from a skill invocation, or merge/publish as a side effect of an audit.

## Report

Return CI system, inspected paths, applicable required checks, candidate SHA, observed results, protection evidence or access limits, and the smallest repairs/checks still needed. For non-GitHub systems, apply the same semantics using their existing tools; do not replace them with GitHub Actions.
