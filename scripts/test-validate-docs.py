#!/usr/bin/env python3
"""Exercise documentation validation in isolated fixtures."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).with_name("validate-docs.py")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def body_for(category: str) -> str:
    if category == "workflows":
        return """## Goal

Produce one bounded result.

### Definition of Done

- The requested result exists.
- Current evidence supports the result.
- Remaining gaps are explicit.

## Workflow

1. Resolve the scope and criteria.
2. Produce and verify the result.
"""
    if category == "capabilities":
        return """## Contract

- Input: A bounded caller scope and current candidate.
- Output: Evidence, result, and remaining work.
- Effects: Read-only inspection.

### Acceptance

- The result addresses the supplied criteria.
- Evidence applies to the current candidate.
- Coverage gaps remain explicit.

## Procedure

1. Inspect the supplied scope.
2. Return the bounded result.
"""
    return """## Principles

- Ground material claims in inspected evidence and label unknowns.
- Keep decisions within the supplied scope and preserve useful autonomy.
- Use the smallest check that can resolve a meaningful uncertainty.
- Report missing proof without representing it as a successful result.
"""


def skill(root: Path, category: str, name: str, description: str, body: str | None = None) -> None:
    write(
        root / category / name / "SKILL.md",
        f"---\nname: {name}\ndescription: {description}\nlicense: MIT\n---\n{body or body_for(category)}",
    )


def catalogs(root: Path, skills: list[tuple[str, str, str]]) -> None:
    rows = "\n".join(
        f"| [{name}]({category}/{name}/SKILL.md) | {description} |"
        for category, name, description in skills
    )
    write(root / "README.md", f"# Catalog\n\n| Skill | Result |\n|---|---|\n{rows}\n\n[Plan](workflows/plan-work/SKILL.md)\n[Guide](guide.md#guide)\n[Template]({{PLACEHOLDER}})\n")
    write(root / "llms.txt", "# Index\n\n" + "\n".join(f"- [{name}]({category}/{name}/SKILL.md)" for category, name, _ in skills) + "\n")
    write(root / "guide.md", "# Guide\n")


def run(root: Path, expected: str | None = None) -> None:
    result = subprocess.run([sys.executable, str(SCRIPT), "--root", str(root)], text=True, capture_output=True)
    if expected is None:
        if result.returncode:
            raise AssertionError(result.stdout + result.stderr)
    elif result.returncode == 0 or expected not in result.stdout:
        raise AssertionError(f"Expected {expected!r}, got:\n{result.stdout}{result.stderr}")


def fixture(root: Path) -> list[tuple[str, str, str]]:
    entries = [
        ("workflows", "plan-work", "A sufficiently specific planning skill description."),
        ("mandatory", "vllnt-thinking-principles", "A sufficiently specific session principle description."),
    ]
    for category, name, description in entries:
        skill(root, category, name, description)
    reference = body_for("capabilities")
    write(root / "references/capabilities/example-review/REFERENCE.md", reference)
    write(root / "references/protocols/quality-validation.md", reference)
    catalogs(root, entries)
    return entries


def local_skill(root: Path) -> Path:
    path = root / ".agents/skills/manage-skill/SKILL.md"
    write(
        path,
        "---\nname: manage-skill\ndescription: Maintain this skill collection with clear contracts and validation.\nmetadata:\n  internal: true\n---\n"
        + body_for("workflows"),
    )
    return path


def main() -> int:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        entries = fixture(root)
        local = local_skill(root)
        run(root)

        for metadata in ("", "metadata:\n  internal: false\n", 'metadata:\n  internal: "true"\n'):
            original = local.read_text(encoding="utf-8")
            write(local, original.replace("metadata:\n  internal: true\n", metadata))
            run(root, "local maintainer requires metadata.internal: true")
            local = local_skill(root)
        run(root)

        local.unlink()
        run(root, "missing required local maintenance skill")
        local = local_skill(root)
        run(root)

        write(local, "# Missing frontmatter\n")
        run(root, "missing opening '---' frontmatter delimiter")
        local = local_skill(root)

        write(local, local.read_text(encoding="utf-8").replace("name: manage-skill", "name: wrong-name"))
        run(root, "name must match folder 'manage-skill'")
        local = local_skill(root)

        write(local, local.read_text(encoding="utf-8").replace("description: Maintain this skill collection with clear contracts and validation.", "description: short"))
        run(root, "description must be a specific scalar string")
        local = local_skill(root)

        write(local, local.read_text(encoding="utf-8").replace("description: Maintain this skill collection with clear contracts and validation.\n", ""))
        run(root, "description must be a specific scalar string")
        local = local_skill(root)

        workflow = root / "workflows/plan-work/SKILL.md"
        skill(root, "workflows", "plan-work", entries[0][2], "# Plan Work\n" + body_for("workflows"))
        run(root, "do not repeat the skill name as an H1 title")
        skill(root, "workflows", "plan-work", entries[0][2])

        skill(
            root,
            "workflows",
            "plan-work",
            entries[0][2],
            "## Goal\n\nProduce one bounded result.\n\n## Workflow\n\n1. Do work.\n\n### Definition of Done\n\n- One.\n- Two.\n- Three.\n",
        )
        run(root, "headings must be")
        skill(root, "workflows", "plan-work", entries[0][2])

        skill(
            root,
            "workflows",
            "plan-work",
            entries[0][2],
            body_for("workflows").replace("- Remaining gaps are explicit.\n", ""),
        )
        run(root, "'Definition of Done' needs 3-5 criteria")
        skill(root, "workflows", "plan-work", entries[0][2])

        capability = root / "references/capabilities/example-review/REFERENCE.md"
        write(capability, body_for("capabilities").replace("- Effects: Read-only inspection.\n", ""))
        run(root, "Contract needs '- Effects:'")
        write(capability, body_for("capabilities"))

        mandatory = root / "mandatory/vllnt-thinking-principles/SKILL.md"
        skill(root, "mandatory", "vllnt-thinking-principles", entries[1][2], "## Goal\n\nThis is not a principle.\n")
        run(root, "headings must be")
        skill(root, "mandatory", "vllnt-thinking-principles", entries[1][2])

        skill(root, "mandatory", "vllnt-thinking-principles", entries[1][2], "## Principles\n\nKeep this short.\n")
        run(root, "Principles needs at least one non-empty principle")
        skill(root, "mandatory", "vllnt-thinking-principles", entries[1][2])

        local.write_text(
            local.read_text(encoding="utf-8").replace("### Definition of Done", "## Workflow\n\n1. Bad order.\n\n### Definition of Done", 1),
            encoding="utf-8",
        )
        run(root, ".agents/skills/manage-skill/SKILL.md: headings must be")
        local = local_skill(root)
        run(root)

        readme = root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "Use [plan-work](workflows/plan-work/SKILL.md).\n", encoding="utf-8")
        run(root)
        catalogs(root, entries)

        readme.write_text(readme.read_text(encoding="utf-8") + "[Missing](missing.md)\n", encoding="utf-8")
        run(root, "missing relative link target 'missing.md'")
        catalogs(root, entries)

        readme.write_text(readme.read_text(encoding="utf-8").replace("guide.md#guide", "guide.md#missing"), encoding="utf-8")
        run(root, "missing anchor '#missing'")
        catalogs(root, entries)

        readme.write_text(readme.read_text(encoding="utf-8").replace("A sufficiently specific planning skill description.", "Different description."), encoding="utf-8")
        run(root, "description does not match metadata")
        catalogs(root, entries)

        skill(root, "mandatory", "vllnt-collaboration-principles", "A sufficiently specific collaboration principle description.")
        run(root, "README.md: missing public skill entry")
        catalogs(root, entries + [("mandatory", "vllnt-collaboration-principles", "A sufficiently specific collaboration principle description.")])

        forbidden = root / "references/capabilities/example-review/SKILL.md"
        write(forbidden, "---\nname: forbidden\ndescription: A sufficiently specific forbidden skill description.\n---\n")
        run(root, "SKILL.md is only allowed in public categories or the local maintainer")
        forbidden.unlink()

        capability.write_text("---\nname: metadata\n---\n" + body_for("capabilities"), encoding="utf-8")
        run(root, "canonical references must not contain skill metadata")
        write(capability, body_for("capabilities"))

        quality = root / "references/protocols/quality-validation.md"
        quality.unlink()
        run(root, "missing canonical quality protocol")
        write(quality, body_for("capabilities"))

        capability.unlink()
        run(root, "contains no canonical REFERENCE.md files")
        write(capability, body_for("capabilities"))

        stale = "- [stale](mandatory/stale/SKILL.md)\n"
        (root / "llms.txt").write_text((root / "llms.txt").read_text(encoding="utf-8") + stale, encoding="utf-8")
        run(root, "stale public skill entry 'mandatory/stale/SKILL.md'")

    print("PASS catalog coverage, links, templates, contracts, criteria, local maintenance, and recovery")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
