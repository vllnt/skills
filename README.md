<div align="center">

# vllnt skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](./#available-skills)
[![Release](https://img.shields.io/github/v/release/vllnt/skills?display_name=tag&sort=semver)](https://github.com/vllnt/skills/releases/latest)

**Compatible with:** Claude Code • OpenCode • Codex • Pi • Windsurf • Cursor • More via [skills.sh](https://skills.sh)

[GitHub](https://github.com/vllnt) • [skills.sh/vllnt](https://skills.sh/vllnt/skills) • [Web](https://vllnt.ai)

</div>

---

## About

Open-source agent skills published by **vllnt**. Reusable capabilities for any AI coding agent, distributed via [skills.sh](https://skills.sh/vllnt/skills).

---

## Installation

```bash
npx skills add vllnt/skills
```

Or install a single skill:

```bash
npx skills add vllnt/skills/regulatory-guard
```

---

## Available Skills

### [Regulatory Guard](./regulatory-guard/) — Web Compliance Audit

Verify a website or web app strictly follows applicable legislation: privacy (GDPR / CCPA / ePrivacy), accessibility (WCAG 2.2 AA / ADA / EAA), consumer & e-commerce (DSA / DMA / CCPA-sale / CAN-SPAM), and AI / content (EU AI Act / copyright / DMCA). Outputs a tiered compliance report with evidence, severity, and remediation.

[View skill documentation →](./regulatory-guard/SKILL.md)

---

## Skill Structure

Each skill is a self-contained folder:

```
skill-name/
├── SKILL.md          # Main skill file (required, with YAML frontmatter)
├── README.md         # Human-facing docs
├── EXAMPLE.md        # Usage examples (optional)
└── references/       # Reference docs loaded on-demand (optional)
```

Skills are agent-agnostic Markdown — no build step.

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Issues and PRs welcome.

---

## License

[MIT](./LICENSE) © 2026 vllnt
