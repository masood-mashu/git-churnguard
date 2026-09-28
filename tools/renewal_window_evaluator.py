"""
renewal_window_evaluator.py - Evaluates account risk tier based on remaining days to contract renewal
"""
import sys
import json


def evaluate_renewal_window(days_to_renewal: int, account_tier: str = "AT_RISK"):
    urgent = days_to_renewal <= 90 and account_tier in ["AT_RISK", "CRITICAL"]
    return {
        "days_to_renewal": days_to_renewal,
        "account_tier": account_tier,
        "urgent_intervention_required": urgent,
        "status": "URGENT_CSM_ENGAGEMENT" if urgent else "STANDARD_CADENCE"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "renewal-window-evaluator"}))
