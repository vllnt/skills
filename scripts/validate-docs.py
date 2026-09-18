#!/usr/bin/env python3
"""Validate public-skill catalogs and local Markdown links for this collection."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CATEGORIES = ("workflows", "mandatory")
LOCAL_MAINTAINER = ".agents/skills/manage-skill/SKILL.md"
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
FIELD = re.compile(r"^(name|description):\s*(.+?)\s*$", re.M)
LIST_ITEM = re.compile(r"^-\s+\S")
FLAT_FIELD = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def scalar(value: str) -> str | None:
    """Parse the flat, single-line string subset used by this collection."""
    value = value.strip()
    lowered = value.lower()
    if not value or value.startswith(("|", ">", "[", "{", "&", "!", "*", "#")):
        return None
    if lowered in {"null", "~", "true", "false", "yes", "no", "on", "off"}:
        return None
    if value.startswith('"') or value.startswith("'"):
        quote = value[0]
        if len(value) < 2 or not value.endswith(quote):
            return None
        value = value[1:-1]
    elif value.endswith(('"', "'")) or ": " in value:
        return None
    return value or None


def validate_local_frontmatter(root: Path, path: Path, errors: list[str]) -> None:
    """Apply the collection's flat frontmatter contract to local maintenance."""
    relative = path.relative_to(root).as_posix()
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail(errors, f"{relative}: missing opening '---' frontmatter delimiter")
        return
    end = content.find("\n---\n", 4)
    if end < 0:
        fail(errors, f"{relative}: frontmatter block missing or unterminated")
        return

    fields: dict[str, str] = {}
    for line in content[4:end].splitlines():
        match = FLAT_FIELD.fullmatch(line)
        if not match:
            fail(errors, f"{relative}: frontmatter must be a flat mapping of single-line strings")
            continue
        key, raw = match.groups()
        value = scalar(raw)
        if value is None:
            fail(errors, f"{relative}: frontmatter field '{key}' must be a non-empty scalar string")
            continue
        if key in fields:
            fail(errors, f"{relative}: duplicate frontmatter field '{key}'")
            continue
        fields[key] = value

    name = fields.get("name")
    description = fields.get("description")
    if name != path.parent.name:
        fail(errors, f"{relative}: name must match folder '{path.parent.name}'")
    if not description or len(description) < 20:
        fail(errors, f"{relative}: description must be a specific scalar string of at least 20 characters")


def public_skills(root: Path, errors: list[str]) -> dict[str, tuple[str, str]]:
    skills: dict[str, tuple[str, str]] = {}
    allowed = {LOCAL_MAINTAINER}
    for category in CATEGORIES:
        directory = root / category
        if not directory.is_dir():
            fail(errors, f"{category}: missing required public category directory")
            continue
        skill_files = sorted(directory.glob("*/SKILL.md"))
        if not skill_files:
            fail(errors, f"{category}: contains no public SKILL.md files")
        for skill_file in skill_files:
            relative = skill_file.relative_to(root).as_posix()
            allowed.add(relative)
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
    for skill_file in root.rglob("SKILL.md"):
        if ".git" in skill_file.parts:
            continue
        relative = skill_file.relative_to(root).as_posix()
        if relative not in allowed:
            fail(errors, f"{relative}: SKILL.md is only allowed in public categories or the local maintainer")
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


def skill_body(path: Path) -> list[tuple[int, str]]:
    """Return the Markdown body after the required YAML frontmatter."""
    content = path.read_text(encoding="utf-8")
    end = content.find("\n---\n", 4)
    if end < 0:
        return []
    body = content[end + 5 :].splitlines()
    lines: list[tuple[int, str]] = []
    fenced = False
    for number, line in enumerate(body, content[: end + 5].count("\n") + 1):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if not fenced:
            lines.append((number, line))
    return lines


def skill_headings(path: Path) -> list[tuple[int, int, str]]:
    headings: list[tuple[int, int, str]] = []
    for line_number, line in skill_body(path):
        match = HEADING.match(line)
        if match:
            level = len(line) - len(line.lstrip("#"))
            headings.append((line_number, level, match.group(1)))
    return headings


def section_lines(path: Path, heading: tuple[int, int, str]) -> list[str]:
    """Return body lines until the next heading of the same or higher level."""
    number, level, _ = heading
    lines = skill_body(path)
    result: list[str] = []
    active = False
    for line_number, line in lines:
        if line_number == number:
            active = True
            continue
        if not active:
            continue
        match = HEADING.match(line)
        if match:
            next_level = len(line) - len(line.lstrip("#"))
            if next_level <= level:
                break
        result.append(line)
    return result


def validate_exact_headings(
    relative: str,
    headings: list[tuple[int, int, str]],
    expected: list[tuple[int, str]],
    errors: list[str],
) -> bool:
    actual = [(level, text) for _, level, text in headings]
    if actual == expected:
        return True
    rendered = " -> ".join("#" * level + " " + text for level, text in actual) or "(none)"
    wanted = " -> ".join("#" * level + " " + text for level, text in expected)
    fail(errors, f"{relative}: headings must be '{wanted}', found '{rendered}'")
    return False


def validate_criteria(relative: str, path: Path, heading: tuple[int, int, str], errors: list[str]) -> None:
    count = sum(bool(LIST_ITEM.match(line)) for line in section_lines(path, heading))
    if not 3 <= count <= 5:
        fail(errors, f"{relative}: '{heading[2]}' needs 3-5 criteria, found {count}")


def validate_skill_structure(root: Path, errors: list[str]) -> None:
    """Keep public skills and the local maintainer on their family templates."""
    targets: list[tuple[str, Path, str]] = []
    for category in CATEGORIES:
        targets.extend((category, path, category) for path in sorted((root / category).glob("*/SKILL.md")))
    local = root / LOCAL_MAINTAINER
    if not local.is_file():
        fail(errors, ".agents/skills/manage-skill/SKILL.md: missing required local maintenance skill")
    else:
        validate_local_frontmatter(root, local, errors)
        targets.append(("local manage-skill", local, "workflow"))

    for category, path, family in targets:
        relative = path.relative_to(root).as_posix()
        headings = skill_headings(path)
        if any(level == 1 for _, level, _ in headings):
            fail(errors, f"{relative}: do not repeat the skill name as an H1 title")
            continue

        if family in ("workflows", "workflow"):
            expected = [(2, "Goal"), (3, "Definition of Done"), (2, "Workflow")]
            if (2, "Boundaries") in [(level, text) for _, level, text in headings]:
                expected.insert(2, (2, "Boundaries"))
            if validate_exact_headings(relative, headings, expected, errors):
                validate_criteria(relative, path, headings[1], errors)
        else:
            expected = [(2, "Principles")]
            if validate_exact_headings(relative, headings, expected, errors):
                if not any(LIST_ITEM.match(line) for line in section_lines(path, headings[0])):
                    fail(errors, f"{relative}: Principles needs at least one non-empty principle")


def reference_headings(path: Path) -> list[tuple[int, int, str]]:
    return [(number, len(line) - len(line.lstrip("#")), match.group(1)) for number, line in markdown_without_fences(path) if (match := HEADING.match(line))]


def reference_section_lines(path: Path, heading: tuple[int, int, str]) -> list[str]:
    result: list[str] = []
    active = False
    for number, line in markdown_without_fences(path):
        if number == heading[0]:
            active = True
            continue
        if not active:
            continue
        match = HEADING.match(line)
        if match and len(line) - len(line.lstrip("#")) <= heading[1]:
            break
        result.append(line)
    return result


def validate_canonical_references(root: Path, errors: list[str]) -> None:
    """Validate canonical contracts without treating them as installed skills."""
    directory = root / "references/capabilities"
    references = sorted(directory.glob("*/REFERENCE.md")) if directory.is_dir() else []
    if not references:
        fail(errors, "references/capabilities: contains no canonical REFERENCE.md files")
    quality = root / "references/protocols/quality-validation.md"
    if quality.is_file():
        references.append(quality)
    else:
        fail(errors, "references/protocols/quality-validation.md: missing canonical quality protocol")
    for path in references:
        relative = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8")
        if content.startswith("---\n") or re.search(r"^(name|description):", content, re.M):
            fail(errors, f"{relative}: canonical references must not contain skill metadata")
        headings = reference_headings(path)
        expected = [(2, "Contract"), (3, "Acceptance"), (2, "Procedure")]
        if headings and headings[-1][1:] == (2, "Pitfalls"):
            expected.append((2, "Pitfalls"))
        if not validate_exact_headings(relative, headings, expected, errors):
            continue
        contract = reference_section_lines(path, headings[0])
        for field in ("Input", "Output", "Effects"):
            if not any(line.startswith(f"- {field}:") for line in contract):
                fail(errors, f"{relative}: Contract needs '- {field}:'")
        count = sum(bool(LIST_ITEM.match(line)) for line in reference_section_lines(path, headings[1]))
        if not 3 <= count <= 5:
            fail(errors, f"{relative}: 'Acceptance' needs 3-5 criteria, found {count}")


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
        skills = public_skills(root, errors)
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
    validate_skill_structure(root, errors)
    validate_canonical_references(root, errors)

    if errors:
        for error in errors:
            print(f"FAIL  {error}")
        print(f"\nDocumentation validation FAILED: {len(errors)} error(s)")
        return 1

    print(f"OK    documentation validated for {len(skills)} public skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
