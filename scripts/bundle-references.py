#!/usr/bin/env python3
"""Copy canonical, on-demand references into each workflow that links to them."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path


LINK = re.compile(r"(?<![!\\])!?\[[^\]]*\]\(([^)]+)\)")
FENCE = re.compile(r"^\s*(```|~~~)")
GENERATED = Path("references/vstack")


class BundleError(Exception):
    pass


def markdown_links(path: Path) -> list[str]:
    """Return Markdown targets outside fenced code blocks."""
    targets: list[str] = []
    fenced = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if FENCE.match(line):
            fenced = not fenced
            continue
        if not fenced:
            targets.extend(match.group(1) for match in LINK.finditer(without_inline_code(line)))
    return targets


def without_inline_code(line: str) -> str:
    """Blank simple inline-code spans so examples cannot become dependencies."""
    result: list[str] = []
    index = 0
    while index < len(line):
        if line[index] != "`":
            result.append(line[index])
            index += 1
            continue
        end = line.find("`", index + 1)
        if end < 0:
            result.append(line[index])
            index += 1
            continue
        result.append(" " * (end - index + 1))
        index = end + 1
    return "".join(result)


def local_target(raw: str) -> str | None:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    # Markdown permits spaces in a destination. Strip an optional quoted title
    # only; unquoted whitespace remains part of the local path.
    title = re.match(r"^(.*?)\s+[\"'](?:[^\"']*)[\"']\s*$", target)
    if title:
        target = title.group(1)
    if not target or target.startswith(("/", "//", "#")):
        return None
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
        return None
    if any(token in target for token in ("{", "}", "<", ">")):
        return None
    return target.split("#", 1)[0] or None


def contained(base: Path, candidate: Path, message: str) -> Path:
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(base.resolve())
    except ValueError as exc:
        raise BundleError(message) from exc
    return resolved


def reject_source(path: Path, references: Path) -> None:
    if path.is_symlink():
        raise BundleError(f"canonical reference is a symlink: {path.relative_to(references)}")
    if path.name == "SKILL.md":
        raise BundleError(f"canonical reference must not be SKILL.md: {path.relative_to(references)}")
    if path.suffix.lower() == ".md" and path.read_text(encoding="utf-8").startswith("---\n"):
        raise BundleError(f"canonical reference has skill frontmatter: {path.relative_to(references)}")


def reject_symlink_path(base: Path, candidate: Path, label: str) -> None:
    """Reject a symlink at any component before resolution erases that evidence."""
    absolute = candidate.absolute()
    try:
        relative = absolute.relative_to(base.absolute())
    except ValueError:
        return
    cursor = base.absolute()
    for part in relative.parts:
        cursor /= part
        if cursor.is_symlink():
            raise BundleError(f"{label} is a symlink: {cursor.relative_to(base.absolute())}")


def reject_tree_symlinks(directory: Path, label: str) -> None:
    """Reject symlinks before a generated-tree write can cross a boundary."""
    if directory.is_symlink():
        raise BundleError(f"{label} is a symlink: {directory}")
    for current, directories, files in os.walk(directory, followlinks=False):
        parent = Path(current)
        for name in [*directories, *files]:
            if (parent / name).is_symlink():
                raise BundleError(f"{label} contains a symlink: {(parent / name).relative_to(directory)}")


def canonical_closure(references: Path, seeds: set[Path]) -> set[Path]:
    """Resolve copied files and reject meaningful canonical Markdown cycles."""
    states: dict[Path, int] = {}
    result: set[Path] = set()

    def parent_reference_backlink(source: Path, destination: Path) -> bool:
        """A nested annex may navigate to its owning REFERENCE without loading it."""
        return (
            destination.name == "REFERENCE.md"
            and source.parent.is_relative_to(destination.parent)
            and source.parent != destination.parent
        )

    def visit(path: Path) -> None:
        reject_symlink_path(references, path, "canonical reference")
        path = contained(references, path, "canonical link escapes references root")
        if not path.is_file():
            raise BundleError(f"missing canonical dependency: {path.relative_to(references)}")
        reject_source(path, references)
        state = states.get(path, 0)
        if state == 1:
            raise BundleError(f"canonical reference cycle: {path.relative_to(references)}")
        if state == 2:
            return
        states[path] = 1
        result.add(path)
        if path.suffix.lower() == ".md":
            for raw in markdown_links(path):
                part = local_target(raw)
                if part is None:
                    continue
                reject_symlink_path(references, path.parent / part, "canonical reference")
                child = contained(
                    references, path.parent / part,
                    f"canonical link escapes references root: {path.relative_to(references)} -> {raw}",
                )
                if not child.is_file():
                    raise BundleError(f"missing canonical dependency: {path.relative_to(references)} -> {raw}")
                # README and nested annex links to their owner are navigation, not loading edges.
                if (path.name == "README.md" or parent_reference_backlink(path, child)) and states.get(child) == 1:
                    continue
                visit(child)
        states[path] = 2

    for seed in sorted(seeds):
        visit(seed)
    return result


def workflow_sources(workflow: Path) -> list[Path]:
    generated = workflow / GENERATED
    return [p for p in sorted(workflow.rglob("*.md")) if generated not in p.parents and p != generated]


def workflow_directories(root: Path) -> list[Path]:
    workflows = root / "workflows"
    if not workflows.is_dir():
        raise BundleError("missing workflows directory")
    return sorted(path for path in workflows.iterdir() if path.is_dir() and (path / "SKILL.md").is_file())


def workflow_seeds(workflow: Path, references: Path) -> set[Path]:
    """Find generated-reference links in workflow prose and validate isolation."""
    generated = workflow / GENERATED
    seeds: set[Path] = set()
    for source in workflow_sources(workflow):
        for raw in markdown_links(source):
            part = local_target(raw)
            if part is None:
                continue
            destination = contained(
                workflow, source.parent / part,
                f"workflow link escapes isolated workflow: {source.relative_to(workflow)} -> {raw}",
            )
            try:
                relative = destination.relative_to(generated.resolve())
            except ValueError:
                if not destination.is_file():
                    raise BundleError(f"missing workflow dependency: {source.relative_to(workflow)} -> {raw}")
                continue
            seeds.add(contained(references, references / relative, "generated reference maps outside references root"))
    return seeds


def expected_tree(root: Path) -> dict[Path, bytes]:
    references = root / "references"
    if references.is_symlink():
        raise BundleError("references root must not be a symlink")
    expected: dict[Path, bytes] = {}
    for workflow in workflow_directories(root):
        reject_tree_symlinks(workflow, f"workflow source {workflow.relative_to(root)}")
        reject_symlink_path(workflow, workflow / GENERATED, "generated subtree")
        if (workflow / GENERATED).is_symlink():
            raise BundleError(f"generated subtree is a symlink: {workflow.relative_to(root)}")
        seeds = workflow_seeds(workflow, references)
        for source in canonical_closure(references, seeds):
            destination = workflow / GENERATED / source.relative_to(references)
            expected[destination] = source.read_bytes()
    return expected


def current_generated(root: Path) -> set[Path]:
    found: set[Path] = set()
    for workflow in workflow_directories(root):
        generated = workflow / GENERATED
        if generated.is_symlink():
            raise BundleError(f"generated subtree is a symlink: {workflow.relative_to(root)}")
        if generated.exists():
            found.update(p for p in generated.rglob("*") if p.is_file() or p.is_symlink())
    return found


def check(root: Path, expected: dict[Path, bytes]) -> list[str]:
    errors: list[str] = []
    actual = current_generated(root)
    for path, content in sorted(expected.items()):
        if not path.is_file() or path.is_symlink():
            errors.append(f"missing generated reference: {path.relative_to(root)}")
        elif path.read_bytes() != content:
            errors.append(f"stale generated reference: {path.relative_to(root)}")
    for path in sorted(actual - set(expected)):
        errors.append(f"unexpected generated reference: {path.relative_to(root)}")
    return errors


def write(root: Path, expected: dict[Path, bytes]) -> None:
    for workflow in workflow_directories(root):
        generated = workflow / GENERATED
        if generated.exists():
            shutil.rmtree(generated)
    for path, content in sorted(expected.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report stale generated references without writing")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        expected = expected_tree(root)
        errors = check(root, expected)
        if args.check:
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 1
            return 0
        write(root, expected)
        return 0
    except BundleError as exc:
        print(f"bundle-references: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
