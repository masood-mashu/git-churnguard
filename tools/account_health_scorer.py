"""
account_health_scorer.py - Calculates unified customer health score based on utilization, support tickets, and NPS
"""
import sys
import json


def score_account_health(health_factors_json: str):
    import json
    data = json.loads(health_factors_json) if isinstance(health_factors_json, str) else health_factors_json
    util = data.get("utilization_pct", 80.0)
    tickets = data.get("open_p1_tickets", 0)
    nps = data.get("nps", 8)
    
    score = (util * 0.5) + (max(10 - (tickets * 3), 0) * 3.0) + (nps * 2.0)
    score = min(max(round(score, 1), 0.0), 100.0)
    tier = "HEALTHY" if score >= 75 else ("AT_RISK" if score >= 50 else "CRITICAL")
    return {
        "health_score": score,
        "tier": tier,
        "status": f"ACCOUNT_{tier}"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "account-health-scorer"}))
