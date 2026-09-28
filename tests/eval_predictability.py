"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitChurnGuard.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.usage_drop_detector import *
from tools.account_health_scorer import *
from tools.renewal_window_evaluator import *

class TestGitChurnGuardPredictability(unittest.TestCase):

    def test_usage_drop_detector(self):
        res = detect_usage_drop('{"baseline_wau": 100, "current_wau": 60}')
        self.assertTrue(res["critical_drop"])
        self.assertEqual(res["status"], "CHURN_RISK_USAGE_DROP")

    def test_account_health_scorer(self):
        res = score_account_health('{"utilization_pct": 90, "open_p1_tickets": 0, "nps": 9}')
        self.assertGreaterEqual(res["health_score"], 75.0)
        self.assertEqual(res["tier"], "HEALTHY")

    def test_renewal_window_evaluator(self):
        res = evaluate_renewal_window(60, account_tier="AT_RISK")
        self.assertTrue(res["urgent_intervention_required"])
        self.assertEqual(res["status"], "URGENT_CSM_ENGAGEMENT")


if __name__ == "__main__":
    unittest.main()
