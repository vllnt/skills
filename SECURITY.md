# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest  | Yes       |
| < Latest | No       |

Only the latest release receives security updates. We recommend always using the most recent version.

## Reporting a Vulnerability

**Do NOT open a public issue for security vulnerabilities.**

### Preferred Method

Use [GitHub Security Advisories](https://github.com/vllnt/skills/security/advisories/new) to privately report vulnerabilities. This creates a private channel between you and the maintainers.

### Alternative

If you cannot use GitHub Security Advisories, contact us via [vllnt.ai](https://vllnt.ai). Include:

- Description of the vulnerability
- Steps to reproduce
- Affected versions
- Potential impact
- Suggested fix (if any)

## Response Timeline

| Stage | Target |
|-------|--------|
| Acknowledgment | Within 48 hours |
| Initial assessment | Within 7 days |
| Patch development | Within 30 days |
| Public disclosure | Within 90 days of report |

We follow a **90-day coordinated disclosure** policy. If a fix is ready sooner, we'll disclose sooner.

## Credit

We credit reporters in:
- Release notes
- Security advisory
- CVE entries (when applicable)

If you prefer to remain anonymous, let us know in your report.

## Scope

In scope:
- Skills published in this repository
- Documentation files that, if tampered with, could mislead agents into unsafe actions

Out of scope:
- Third-party agent runtimes (Claude Code, OpenCode, Cursor, etc.)
- The `skills.sh` distribution platform (report to its maintainers)
