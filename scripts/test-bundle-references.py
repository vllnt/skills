#!/usr/bin/env python3
"""Fixture tests for bundle-references.py; no repository files are changed."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).with_name("bundle-references.py")


def put(root: Path, name: str, content: str) -> Path:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def run(root: Path, *args: str, ok: bool = True) -> str:
    result = subprocess.run([sys.executable, str(SCRIPT), "--root", str(root), *args], text=True, capture_output=True)
    if (result.returncode == 0) != ok:
        raise AssertionError(f"args={args} stdout={result.stdout} stderr={result.stderr}")
    return result.stderr


def base(root: Path, workflow: str = "build-one") -> None:
    put(root, f"workflows/{workflow}/SKILL.md", "[reference](references/vstack/capabilities/topic/REFERENCE.md)\n")
    put(root, "references/capabilities/topic/REFERENCE.md", "# Topic\n\n[annex](annex/detail.md)\n![image](annex/card.txt)\n")
    put(root, "references/capabilities/topic/annex/detail.md", "# Detail\n")
    put(root, "references/capabilities/topic/annex/card.txt", "asset\n")


def expect_failure(root: Path, phrase: str) -> None:
    output = run(root, "--check", ok=False)
    assert phrase in output, output


def test_bundle_and_check() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        run(root, "--check", ok=False)
        run(root)
        run(root, "--check")
        copied = root / "workflows/build-one/references/vstack/capabilities/topic/annex/detail.md"
        assert copied.read_text(encoding="utf-8") == "# Detail\n"
        assert (root / "workflows/build-one/references/vstack/capabilities/topic/annex/card.txt").is_file()
        # A source edit is stale until a write recovers the byte-identical copy.
        put(root, "references/capabilities/topic/annex/detail.md", "# Changed\n")
        assert "stale generated reference" in run(root, "--check", ok=False)
        run(root)
        assert copied.read_text(encoding="utf-8") == "# Changed\n"


def test_unexpected_and_deleted_source() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        run(root)
        put(root, "workflows/build-one/references/vstack/unused.md", "old\n")
        assert "unexpected generated reference" in run(root, "--check", ok=False)
        run(root)
        assert not (root / "workflows/build-one/references/vstack/unused.md").exists()
        (root / "references/capabilities/topic/annex/detail.md").unlink()
        expect_failure(root, "missing canonical dependency")


def test_hand_reference_seed_and_isolation() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        put(root, "workflows/build-one/references/guide.md", "[load](vstack/capabilities/topic/REFERENCE.md)\n")
        put(root, "workflows/build-one/SKILL.md", "[guide](references/guide.md)\n")
        run(root)
        put(root, "workflows/build-one/references/guide.md", "[bad](../../../outside.md)\n")
        expect_failure(root, "workflow link escapes isolated workflow")


def test_cycles_escapes_and_metadata() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        put(root, "references/capabilities/topic/annex/detail.md", "[next](other.md)\n")
        put(root, "references/capabilities/topic/annex/other.md", "[back](detail.md)\n")
        expect_failure(root, "canonical reference cycle")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        put(root, "references/capabilities/topic/REFERENCE.md", "[bad](../../../outside.md)\n")
        expect_failure(root, "canonical link escapes references root")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        put(root, "references/capabilities/topic/REFERENCE.md", "---\nname: no\n---\n")
        expect_failure(root, "skill frontmatter")


def test_readme_backlink_and_fenced_links() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        put(root, "references/capabilities/topic/REFERENCE.md", "[readme](README.md)\n```md\n[ignored](missing.md)\n```\n")
        put(root, "references/capabilities/topic/README.md", "[back](REFERENCE.md)\n")
        run(root)
        run(root, "--check")


def test_annex_backlink_is_navigation() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        put(root, "references/capabilities/topic/annex/detail.md", "[owner](../REFERENCE.md)\n")
        run(root)
        run(root, "--check")


def test_skill_file_and_symlink_rejected() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        put(root, "references/capabilities/topic/REFERENCE.md", "[skill](SKILL.md)\n")
        put(root, "references/capabilities/topic/SKILL.md", "plain\n")
        expect_failure(root, "must not be SKILL.md")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        target = root / "references/capabilities/topic/annex/real.md"
        target.write_text("# Real\n", encoding="utf-8")
        link = root / "references/capabilities/topic/annex/detail.md"
        link.unlink()
        link.symlink_to(target)
        expect_failure(root, "canonical reference is a symlink")


def test_inline_escaped_and_spaced_links() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        put(
            root,
            "references/capabilities/topic/REFERENCE.md",
            "`[example](missing.md)` \\[escaped](also-missing.md) [space](annex/with space.md)\n",
        )
        put(root, "references/capabilities/topic/annex/with space.md", "# Space\n")
        run(root)
        assert (root / "workflows/build-one/references/vstack/capabilities/topic/annex/with space.md").is_file()
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        source = root / "workflows/build-one/references/linked.md"
        source.parent.mkdir(parents=True, exist_ok=True)
        source.symlink_to(root / "references/capabilities/topic/REFERENCE.md")
        expect_failure(root, "workflow source workflows/build-one contains a symlink")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        references = root / "workflows/build-one/references"
        references.mkdir()
        references.rmdir()
        references.symlink_to(root / "references")
        expect_failure(root, "workflow source workflows/build-one contains a symlink")


def test_non_workflow_cannot_expand_write_scope() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        base(root)
        external = root / "external/vstack"
        external.mkdir(parents=True)
        marker = external / "keep.md"
        marker.write_text("keep\n", encoding="utf-8")
        references = root / "workflows/not-a-workflow/references"
        references.parent.mkdir(parents=True)
        references.symlink_to(root / "external")
        run(root)
        assert marker.read_text(encoding="utf-8") == "keep\n"


def main() -> int:
    test_bundle_and_check()
    test_unexpected_and_deleted_source()
    test_hand_reference_seed_and_isolation()
    test_cycles_escapes_and_metadata()
    test_readme_backlink_and_fenced_links()
    test_annex_backlink_is_navigation()
    test_skill_file_and_symlink_rejected()
    test_inline_escaped_and_spaced_links()
    test_non_workflow_cannot_expand_write_scope()
    print("PASS bundle references: closure, recovery, isolation, and invalid graphs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
