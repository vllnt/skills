#!/usr/bin/env python3
"""Validate public-skill catalogs and local Markdown links for this collection."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CATEGORIES = ("workflows", "capabilities", "mandatory")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
FIELD = re.compile(r"^(name|description):\s*(.+?)\s*$", re.M)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def public_skills(root: Path) -> dict[str, tuple[str, str]]:
    skills: dict[str, tuple[str, str]] = {}
    for category in CATEGORIES:
        directory = root / category
        for skill_file in sorted(directory.glob("*/SKILL.md")):
            relative = skill_file.relative_to(root).as_posix()
            content = skill_file.read_text(encoding="utf-8")
            if not content.startswith("---\n"):
                raise ValueError(f"{relative}: missing frontmatter")
            end = content.find("\n---\n", 4)
            if end < 0:
                raise ValueError(f"{relative}: unterminated frontmatter")
            header = content[4:end]
            fields = dict(FIELD.findall(header))
            name = fields.get("name")
            description = fields.get("description")
            if not name or not description:
                raise ValueError(f"{relative}: missing name or description")
            skills[relative] = (name.strip("\"'"), description.strip("\"'"))
    return skills


def markdown_without_fences(path: Path) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    fenced = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if not fenced:
            lines.append((number, line))
    return lines


def slug(value: str) -> str:
    value = re.sub(r"[`*_~]", "", value).lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def anchors(path: Path) -> set[str]:
    return {
        slug(match.group(1))
        for _, line in markdown_without_fences(path)
        if (match := HEADING.match(line))
    }


def is_placeholder(target: str) -> bool:
    return "{" in target or "}" in target or "<" in target or ">" in target


def is_external(target: str) -> bool:
    return bool(re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("//"))


def resolve_link(root: Path, source: Path, raw_target: str) -> tuple[Path | None, str | None]:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split(" ", 1)[0]
    if is_external(target) or is_placeholder(target) or target.startswith("/"):
        return None, None
    file_part, separator, anchor = target.partition("#")
    destination = source if not file_part else (source.parent / file_part).resolve()
    try:
        destination.relative_to(root)
    except ValueError:
        return None, None
    return destination, anchor if separator else None


def validate_links(root: Path, errors: list[str]) -> None:
    for source in sorted(root.rglob("*.md")):
        if ".git" in source.parts:
            continue
        for line_number, line in markdown_without_fences(source):
            for match in LINK.finditer(line):
                raw_target = match.group(1)
                destination, anchor = resolve_link(root, source, raw_target)
                if destination is None:
                    continue
                label = f"{source.relative_to(root)}:{line_number}"
                if not destination.is_file():
                    fail(errors, f"{label}: missing relative link target '{raw_target}'")
                elif anchor and slug(anchor) not in anchors(destination):
                    fail(errors, f"{label}: missing anchor '#{anchor}' in '{destination.relative_to(root)}'")


def links_to_public_skills(path: Path, root: Path) -> set[str]:
    found: set[str] = set()
    for _, line in markdown_without_fences(path):
        for match in LINK.finditer(line):
            destination, _ = resolve_link(root, path, match.group(1))
            if destination and destination.name == "SKILL.md":
                try:
                    relative = destination.relative_to(root).as_posix()
                except ValueError:
                    continue
                if relative.split("/", 1)[0] in CATEGORIES:
                    found.add(relative)
    return found


def validate_readme_descriptions(root: Path, skills: dict[str, tuple[str, str]], errors: list[str]) -> None:
    readme = root / "README.md"
    for line_number, line in markdown_without_fences(readme):
        match = LINK.search(line)
        if not match or "/SKILL.md" not in match.group(1):
            continue
        destination, _ = resolve_link(root, readme, match.group(1))
        if not destination:
            continue
        relative = destination.relative_to(root).as_posix()
        if relative not in skills:
            continue
        if not (line.lstrip().startswith("|") and line.rstrip().endswith("|")):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            fail(errors, f"README.md:{line_number}: public skill link needs a description table cell")
            continue
        label = re.search(r"\[([^\]]+)\]", cells[0])
        name, description = skills[relative]
        # Folder overviews may link several skills in another cell. Only a
        # first-cell skill row is the catalog whose wording must match metadata.
        if not label:
            continue
        if label.group(1) != name:
            fail(errors, f"README.md:{line_number}: label does not match metadata name for '{relative}'")
        if cells[1].rstrip(".") != description.rstrip("."):
            fail(errors, f"README.md:{line_number}: description does not match metadata for '{relative}'")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    arguments = parser.parse_args()
    root = arguments.root.resolve()
    errors: list[str] = []

    try:
        skills = public_skills(root)
    except ValueError as exception:
        fail(errors, str(exception))
        skills = {}

    for catalog_name in ("README.md", "llms.txt"):
        catalog = root / catalog_name
        catalog_paths = links_to_public_skills(catalog, root)
        for path in sorted(skills.keys() - catalog_paths):
            fail(errors, f"{catalog_name}: missing public skill entry '{path}'")
        for path in sorted(catalog_paths - skills.keys()):
            fail(errors, f"{catalog_name}: stale public skill entry '{path}'")

    validate_readme_descriptions(root, skills, errors)
    validate_links(root, errors)

    if errors:
        for error in errors:
            print(f"FAIL  {error}")
        print(f"\nDocumentation validation FAILED: {len(errors)} error(s)")
        return 1

    print(f"OK    documentation validated for {len(skills)} public skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
