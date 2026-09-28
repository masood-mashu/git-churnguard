"""
usage_drop_detector.py - Calculates percentage drop in weekly active users compared to previous 30-day baseline
"""
import sys
import json


def detect_usage_drop(usage_data_json: str, drop_threshold_pct: float = 30.0):
    import json
    data = json.loads(usage_data_json) if isinstance(usage_data_json, str) else usage_data_json
    base = max(data.get("baseline_wau", 100), 1)
    curr = data.get("current_wau", 100)
    drop_pct = ((base - curr) / base) * 100.0 if curr < base else 0.0
    is_critical = drop_pct >= drop_threshold_pct
    return {
        "baseline_wau": base,
        "current_wau": curr,
        "drop_percentage": round(drop_pct, 2),
        "critical_drop": is_critical,
        "status": "CHURN_RISK_USAGE_DROP" if is_critical else "USAGE_STABLE"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "usage-drop-detector"}))
