#!/usr/bin/env python3
"""Exercise the exact notification workflow shell without GitHub side effects."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / ".github/workflows/notify-stack.yml").read_text()
# Deliberately narrow: one inline shell block, no new YAML parser dependency.
SCRIPT = textwrap.dedent(WORKFLOW.split("        run: |\n", 1)[1])


class NotificationTests(unittest.TestCase):
    def invoke(self, token="synthetic-test-token", status=0):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fake = root / "gh"
            fake.write_text("#!/usr/bin/env python3\nimport json, os, sys\n"
                            "from pathlib import Path\n"
                            "with Path(os.environ['CALL_LOG']).open('a') as log:\n"
                            "    log.write(json.dumps(sys.argv[1:]) + '\\n')\n"
                            "sys.exit(int(os.environ['FAKE_STATUS']))\n")
            fake.chmod(0o755)
            env = {**os.environ, "PATH": f"{root}{os.pathsep}{os.environ['PATH']}",
                   "GH_TOKEN": token, "FAKE_STATUS": str(status), "CALL_LOG": str(root / "calls.json"),
                   "INPUT_SHA": "attacker-controlled-value", "INPUT_REPO": "untrusted/target"}
            result = subprocess.run(["bash", "-c", SCRIPT], env=env, text=True, capture_output=True, timeout=10)
            log = root / "calls.json"
            return result, [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []

    def test_trusted_trigger_and_secret_boundary(self):
        self.assertIn("branches: [main]", WORKFLOW)
        self.assertIn("workflow_dispatch:", WORKFLOW)
        self.assertNotIn("pull_request", WORKFLOW)
        self.assertIn("github.repository == 'vllnt/skills' && github.ref == 'refs/heads/main'", WORKFLOW)
        self.assertIn("permissions: {}", WORKFLOW)
        self.assertIn("cancel-in-progress: false", WORKFLOW)
        self.assertIn("timeout-minutes: 3", WORKFLOW)
        self.assertEqual(WORKFLOW.count("secrets."), 1)
        self.assertIn("secrets.STACK_UPDATE_TOKEN", WORKFLOW)
        self.assertNotIn("${{", SCRIPT)
        self.assertNotIn("set -x", SCRIPT)

    def test_fixed_dispatch_without_payload_or_secret_output(self):
        result, args = self.invoke()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(args, [["api", "--method", "POST", "repos/vllnt/stack/dispatches",
                                 "--raw-field", "event_type=skills-updated"]])
        self.assertNotIn("synthetic-test-token", result.stdout + result.stderr)
        self.assertIn("Sent skills-updated", result.stdout)

    def test_missing_token_does_not_dispatch(self):
        result, args = self.invoke(token="")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(args, [])
        self.assertNotIn("Sent skills-updated", result.stdout)

    def test_api_failure_is_not_a_success_or_retried(self):
        result, args = self.invoke(status=42)
        self.assertEqual(result.returncode, 42)
        self.assertEqual(len(args), 1)
        self.assertNotIn("Sent skills-updated", result.stdout)


if __name__ == "__main__":
    unittest.main()
