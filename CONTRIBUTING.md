# Contributing to vllnt skills

Thanks for your interest in contributing! This guide explains how to get involved.

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## How to Contribute

### Reporting Bugs

1. Check [existing issues](https://github.com/vllnt/skills/issues) first
2. Use the [bug report template](https://github.com/vllnt/skills/issues/new?template=bug_report.yml)
3. Include: steps to reproduce, expected vs actual behavior, environment details, relevant logs

### Suggesting Features

1. Check [existing requests](https://github.com/vllnt/skills/issues?q=label%3Aenhancement)
2. Use the [feature request template](https://github.com/vllnt/skills/issues/new?template=feature_request.yml)
3. Describe the problem you're solving, not just the solution

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Make your changes
4. Update `CHANGELOG.md` (CI requires it on every PR)
5. Commit using [conventional commits](https://www.conventionalcommits.org/):
   - `feat: add new feature`
   - `fix: resolve bug`
   - `docs: update documentation`
   - `chore: maintenance task`
6. Push and open a Pull Request against `main`

## Development Setup

```bash
git clone https://github.com/vllnt/skills.git
cd skills
```

No build step required — skills are pure Markdown files.

## Skill Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md          # Main skill file (required)
├── README.md         # Skill documentation
├── references/       # Reference docs loaded on-demand
└── EXAMPLE.md        # Usage examples (optional)
```

### Key Conventions

- `SKILL.md` must include valid YAML frontmatter (`name`, `description`)
- Reference files are loaded by the action router, not eagerly
- Skills must be agent-agnostic (Claude Code, OpenCode, Cursor, etc.)
- Use relative paths for cross-references within a skill
- Skills must NOT cross-reference other skills (independence)

## Pull Request Guidelines

- Keep PRs focused — one skill or feature per PR
- Update the skill's `README.md` for any behavior changes
- Update root `CHANGELOG.md` (BLOCKING — CI enforces this)
- Follow existing patterns in similar skills
- Request review from maintainers

## First-Time Contributors

Look for issues labeled [`good first issue`](https://github.com/vllnt/skills/labels/good%20first%20issue).

## Community

- [GitHub](https://github.com/vllnt) — issues, PRs, code
- [Web](https://bntvllnt.com) — about the maintainers and projects

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT).
