#!/usr/bin/env python3
"""Exercise real Skills CLI discovery: python3 scripts/test-skill-discovery.py CLI.mjs."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def main():
    cli = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parent.parent
    expected = {
        p.parent.name
        for category in ("workflows", "mandatory")
        for p in (repo / category).glob("*/SKILL.md")
    }
    env = dict(os.environ, DISABLE_TELEMETRY="1")
    env.pop("INSTALL_INTERNAL_SKILLS", None)
    with tempfile.TemporaryDirectory(prefix="skill-discovery-") as directory:
        root = Path(directory)
        for category in ("workflows", "mandatory", ".agents"):
            shutil.copytree(repo / category, root / category)

        def discover():
            result = subprocess.run(
                ["node", str(cli), "add", str(root), "--list"],
                env=env, capture_output=True, text=True, timeout=60, check=True,
            )
            output = re.sub(r"\x1b\[[0-9;?]*[A-Za-z]", "", result.stdout)
            return set(re.findall(r"^│\s{4}([a-z][a-z0-9-]*)\s*$", output, re.M))

        local = root / ".agents/skills/manage-skill/SKILL.md"
        fixed = local.read_text()
        local.write_text(fixed.replace("metadata:\n  internal: true\n", ""))
        assert discover() == {"manage-skill"}, "Expected pre-fix discovery failure"
        local.write_text(fixed)
        assert discover() == expected, "Default discovery must expose exactly public skills"
        print(f"PASS real CLI: pre-fix only maintainer; fixed {len(expected)} public skills")


if __name__ == "__main__":
    main()
