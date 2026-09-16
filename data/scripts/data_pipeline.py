import pandas as pd

# 1. Load public health dataset
df = pd.read_csv("data/sample_health_data.csv")

# 2. Process metrics: Calculate target compliance rate by county
county_summary = df.groupby("county").agg(
    total_reports=("reports_submitted", "sum"),
    targets_achieved=("target_met", lambda x: (x == "Yes").sum())
).reset_index()

# 3. Output results summary
print(" Amref Project Performance Summary ")
print(county_summary)
