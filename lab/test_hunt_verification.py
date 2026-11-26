"""Fail-closed checks for the generator's existing hunt audit claims.

These synthetic mutations test the verifier, not a learner or the authored
Hunt 03/05 story. They deliberately do not change the generated events.
"""

import copy
import datetime
from contextlib import redirect_stdout
import io
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest


Generator = runpy.run_path(str(Path(__file__).with_name("generate-hunt-telemetry.py")))[
    "HarrowmereTelemetryGenerator"
]


class HuntVerificationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = Generator(
            total_events=250,
            days=14,
            seed=42,
            start_time=datetime.datetime(2026, 9, 1),
        )
        with redirect_stdout(io.StringIO()):
            cls.baseline.generate_all()

    def verify(self, case):
        with redirect_stdout(io.StringIO()):
            case.run_verification()

    def test_known_seed_passes_existing_verification(self):
        self.verify(self.baseline)

    def test_missing_beacons_cannot_skip_jitter_audit(self):
        case = copy.copy(self.baseline)
        case.conn_logs = [
            event for event in self.baseline.conn_logs
            if not (event["source.ip"] == "10.100.14.88"
                    and event["destination.ip"] == "198.51.100.84")
        ]
        with self.assertRaisesRegex(AssertionError, "Beacon events"):
            self.verify(case)

    def test_rare_user_agent_cannot_have_multiple_host_sources(self):
        case = copy.copy(self.baseline)
        cargo = next(event for event in self.baseline.http_logs
                     if event["user_agent.original"].startswith("cargo/"))
        case.http_logs = [*self.baseline.http_logs, {**cargo, "source.ip": "10.100.42.19"}]
        with self.assertRaisesRegex(AssertionError, "Host cardinality"):
            self.verify(case)

    def test_missing_benign_dns_cannot_claim_entropy_discrimination(self):
        case = copy.copy(self.baseline)
        case.dns_logs = [
            event for event in self.baseline.dns_logs
            if "data-relay" in event["dns.question.name"]
            or "data-sync" in event["dns.question.name"]
        ]
        with self.assertRaisesRegex(AssertionError, "Benign DNS baseline"):
            self.verify(case)

    def test_optimized_python_cannot_turn_off_verification(self):
        # -O removes assert statements entirely. A zero-head case has no
        # benign DNS baseline and must never print an unconditional PASS.
        with tempfile.TemporaryDirectory() as output:
            result = subprocess.run(
                [sys.executable, "-O", str(Path(__file__).with_name("generate-hunt-telemetry.py")),
                 "--count", "0", "--seed", "42", "--start-date", "2026-09-01",
                 "--format", "ndjson", "--out-dir", output, "--verify"],
                capture_output=True, text=True, timeout=60, check=False,
            )
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Benign DNS baseline missing", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
