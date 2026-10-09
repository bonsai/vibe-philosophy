import csv
import io
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stdout, redirect_stderr
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("experiment_optimizer", ROOT / "scripts" / "experiment_optimizer.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

FIELDS = ["experiment_id","task_id","model_id","model_version","instruction_id","instruction_version",
          "agent_config_id","run_id","axis","score","latency_ms","input_tokens","output_tokens",
          "total_cost","currency","critical_failure","evidence_ref","reviewer","review_status","decision"]

def sample_rows():
    rows = []
    scores = {"ethics":5,"speed":4,"capability":4,"accuracy":4,"cost":4,"depth":4}
    for run in ("run-1","run-2","run-3"):
        for axis, score in scores.items():
            rows.append({"experiment_id":"EXP-1","task_id":"TASK-1","model_id":"demo/model",
                         "model_version":"v1","instruction_id":"INST-1","instruction_version":"v1",
                         "agent_config_id":"CFG-1","run_id":run,"axis":axis,"score":str(score),
                         "latency_ms":"500","input_tokens":"100","output_tokens":"50","total_cost":"0.01",
                         "currency":"USD","critical_failure":"no","evidence_ref":"artifact://run",
                         "reviewer":"independent-reviewer","review_status":"approved","decision":"PASS"})
    return rows

class OptimizerTests(unittest.TestCase):
    def run_csv(self, rows):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.csv"
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                code = MOD.main([str(path), "--json"])
            return code, out.getvalue(), err.getvalue()

    def test_three_reviewed_complete_runs_are_eligible(self):
        code, output, _ = self.run_csv(sample_rows())
        self.assertEqual(code, 0)
        self.assertIn('"agent_config_id": "CFG-1"', output)

    def test_ethics_failure_is_rejected(self):
        rows = sample_rows()
        rows[0]["critical_failure"] = "yes"
        code, output, _ = self.run_csv(rows)
        self.assertNotEqual(code, 0)
        self.assertIn("critical failure", output)

    def test_missing_axis_prevents_eligibility(self):
        rows = sample_rows()[:-1]
        code, output, _ = self.run_csv(rows)
        self.assertNotEqual(code, 0)
        self.assertIn("missing axes", output)

    def test_unapproved_review_is_rejected(self):
        rows = sample_rows()
        rows[0]["review_status"] = "pending"
        code, output, _ = self.run_csv(rows)
        self.assertNotEqual(code, 0)
        self.assertIn("review_status must be approved", output)

if __name__ == "__main__":
    unittest.main()
