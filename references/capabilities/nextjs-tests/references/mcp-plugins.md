# Optional Next.js integrations

Discover exposed tools and installed versions before use. No MCP plugin is required, and discovery does not grant credentials, production access or permission to mutate state.

| Capability | Optional integration | Equivalent evidence |
|---|---|---|
| Browser behavior | Browser MCP or agent-browser | Repository browser runner or authorized manual browser evidence |
| Next.js diagnostics | Next.js DevTools MCP | App logs, browser errors, repository build and tests |
| Deployment status | Deployment-provider MCP | Existing provider CLI/API, CI checks and deployment logs |
| Framework docs | Documentation MCP | Installed docs or version-matched official docs fetched on demand |
| Design comparison | Design-provider MCP | Supplied design exports/specs and actual browser screenshots |

## Server discovery

If Next.js DevTools exposes server discovery, match the selected instance to the repository workspace, app and running command. Confirm its URL/port from launch output and configuration. Never choose `servers[0]` or the first global `next dev` process. Use only diagnostic tools appropriate to the installed version; cache clearing or other mutations require scope and authority.

## Deployment verification

Match a preview to the intended project and candidate commit, not just a reusable branch name. Read deployment status and logs with existing authorized access. A ready deployment or successful HTTP fetch is infrastructure evidence, not browser verification. Protected previews require legitimate access; do not bypass protection. Missing provider tools need not prevent local tests or source review.

## Documentation and design

Resolve documentation for the installed Next.js release, especially caching, routing and Server Actions. Prefer existing design files or supplied exports if a design plugin is absent. State missing visual evidence rather than inventing design conformance.

## Recovery

Classify failures: app defect, unsupported tool/version, missing local prerequisite, or external access. Repair authorized reversible local prerequisites and switch to equivalent tools. Avoid automatic global installs or remote latest-version downloads. If access remains unavailable, provide completed findings and the exact remaining check/access owner; do not require installation of a particular vendor tool.
