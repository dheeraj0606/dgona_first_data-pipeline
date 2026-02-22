import json
from datetime import datetime
import pandas as pd

def generate_summary(file_path: str, status: str):
    df = pd.read_csv(file_path)

    summary = {
        "timestamp": datetime.utcnow().isoformat(),
        "total_rows": len(df),
        "total_revenue": float((df["quantity"] * df["price"]).sum()),
        "status": status
    }

    with open("pipeline_run_summary.json", "w") as f:
        json.dump(summary, f, indent=4)

    return summary
