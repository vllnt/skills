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


def skill(root: Path, category: str, name: str, description: str) -> None:
    write(
        root / category / name / "SKILL.md",
        f"---\nname: {name}\ndescription: {description}\nlicense: MIT\n---\n# {name}\n",
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
        ("capabilities", "capability-example-review", "A sufficiently specific internal review description."),
        ("mandatory", "vllnt-thinking-principles", "A sufficiently specific session principle description."),
    ]
    for category, name, description in entries:
        skill(root, category, name, description)
    catalogs(root, entries)
    return entries


def main() -> int:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        entries = fixture(root)
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

        stale = "- [stale](mandatory/stale/SKILL.md)\n"
        (root / "llms.txt").write_text((root / "llms.txt").read_text(encoding="utf-8") + stale, encoding="utf-8")
        run(root, "stale public skill entry 'mandatory/stale/SKILL.md'")

    print("PASS catalog coverage, metadata descriptions, local links, anchors, placeholders, and recovery")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
