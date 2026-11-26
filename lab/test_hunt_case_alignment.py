"""Contract tests: synthetic case evidence must support the authored Hunts 03/05."""

import datetime
import io
import math
from contextlib import redirect_stdout
from pathlib import Path
import runpy
import unittest


Generator = runpy.run_path(str(Path(__file__).with_name("generate-hunt-telemetry.py")))[
    "HarrowmereTelemetryGenerator"
]


class HuntCaseAlignmentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = Generator(total_events=250, days=14, seed=17,
                             start_time=datetime.datetime(2026, 9, 1))
        with redirect_stdout(io.StringIO()):
            cls.case.generate_all()

    def test_hunt03_is_a_distinct_tls_case_with_642_sessions(self):
        rows = [r for r in self.case.conn_logs
                if r["source.ip"] == "10.42.18.91"
                and r["destination.ip"] == "198.51.100.84"]
        self.assertEqual(len(rows), 642)
        self.assertEqual({r["destination.port"] for r in rows}, {443})
        self.assertEqual({r["service"] for r in rows}, {"ssl"})
        hunt02 = [r for r in self.case.conn_logs
                  if r["source.ip"] == "10.100.14.88"
                  and r["destination.ip"] == "198.51.100.84"]
        self.assertTrue(hunt02)
        self.assertEqual({r["destination.port"] for r in hunt02}, {8080})

    def test_hunt05_chicago_c2_matches_timing_and_fingerprint(self):
        rows = sorted((r for r in self.case.conn_logs
                       if r["source.ip"] == "10.120.32.14"
                       and r["destination.ip"] == "198.51.100.84"),
                      key=lambda r: r["@timestamp"])
        self.assertEqual(len(rows), 3840)
        self.assertEqual({r["destination.port"] for r in rows}, {443})
        timestamps = [datetime.datetime.strptime(r["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
                      for r in rows]
        intervals = [(b - a).total_seconds() for a, b in zip(timestamps, timestamps[1:])]
        mean = sum(intervals) / len(intervals)
        sd = math.sqrt(sum((x - mean) ** 2 for x in intervals) / len(intervals))
        self.assertAlmostEqual(mean, 300.2, delta=2.0)
        self.assertAlmostEqual(sd, 24.1, delta=1.5)
        self.assertAlmostEqual(sd / mean, 0.08, delta=0.01)
        tls = [r for r in self.case.ssl_logs
               if r["source.ip"] == "10.120.32.14"
               and r["destination.ip"] == "198.51.100.84"]
        self.assertEqual(len(tls), 3840)
        self.assertEqual(len({r["tls.ja4"] for r in tls}), 1)

    def test_hunt05_has_22_smb_and_rpc_sessions(self):
        rows = [r for r in self.case.conn_logs
                if r["source.ip"] == "10.120.32.14"
                and r["destination.ip"] == "10.110.16.5"]
        self.assertEqual(len(rows), 22)
        self.assertEqual({r["destination.port"] for r in rows}, {445, 135})
        self.assertEqual({r["service"] for r in rows}, {"smb", "rpc"})

    def test_default_is_explicitly_a_small_dns_preview(self):
        rows = [r for r in self.case.dns_logs
                if r["dns.question.name"].endswith(".data-sync-telemetry.net")]
        self.assertEqual(len(rows), 2500)
        self.assertEqual({r["dns.question.type"] for r in rows}, {"TXT"})
        self.assertTrue(all(len(r["dns.question.name"].split(".")[0]) == 62
                            for r in rows))

    def test_full_hunt05_mode_matches_narrative_dns_count(self):
        full = Generator(total_events=0, days=14, seed=17,
                         start_time=datetime.datetime(2026, 9, 1),
                         full_hunt05=True)
        with redirect_stdout(io.StringIO()):
            full.generate_all()
        rows = [r for r in full.dns_logs
                if r["dns.question.name"].endswith(".data-sync-telemetry.net")]
        self.assertEqual(len(rows), 142890)
        self.assertTrue(all(r["dns.question.type"] == "TXT" for r in rows))
        self.assertAlmostEqual(sum(r["entropy"] for r in rows) / len(rows), 4.86, delta=0.02)


if __name__ == "__main__":
    unittest.main()
