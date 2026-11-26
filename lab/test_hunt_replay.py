"""Protect replayable synthetic hunt cases from accidental nondeterminism.

Equal inputs must yield byte-identical case material. This tests the generator,
not learner performance or the quality of any analyst's judgment.
"""

import gzip
import hashlib
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest


GENERATOR = Path(__file__).with_name("generate-hunt-telemetry.py")
FILES = (
    "hunt_telemetry.db",
    "conn.ndjson.gz",
    "dns.ndjson.gz",
    "http.ndjson.gz",
    "ssl.ndjson.gz",
)


class ReplayableHuntCaseTest(unittest.TestCase):
    def test_seeded_case_replays_across_sqlite_and_gzip(self):
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)

            def generate(name, seed):
                destination = root / name
                result = subprocess.run(
                    [
                        sys.executable,
                        str(GENERATOR),
                        "--count", "250",
                        "--days", "14",
                        "--seed", str(seed),
                        "--start-date", "2026-09-01",
                        "--format", "all",
                        "--out-dir", str(destination),
                        "--verify",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=90,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("ALL AUDIT CHECKS PASSED", result.stdout)
                hashes = {}
                for filename in FILES:
                    path = destination / filename
                    self.assertTrue(path.is_file(), filename)
                    self.assertGreater(path.stat().st_size, 0, filename)
                    hashes[filename] = hashlib.sha256(path.read_bytes()).hexdigest()
                with gzip.open(destination / "conn.ndjson.gz", "rt", encoding="utf-8") as records:
                    self.assertTrue(records.readline().startswith("{"))
                with sqlite3.connect(destination / "hunt_telemetry.db") as database:
                    self.assertGreater(database.execute("SELECT COUNT(*) FROM conn_log").fetchone()[0], 0)
                return hashes

            baseline = generate("first", 42)
            repeated = generate("second", 42)
            different = generate("third", 43)
            self.assertEqual(baseline, repeated, "Same seed and date must replay byte-for-byte")
            self.assertNotEqual(baseline, different, "Changing the seed should change the case")


if __name__ == "__main__":
    unittest.main()
