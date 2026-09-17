from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).resolve().parents[1]
src = PROJECT_ROOT/"data"/"processed"
dst = PROJECT_ROOT/"powerbi_data"
dst.mkdir(parents=True, exist_ok=True)

for name in [
    "mart_sales_summary.csv",
    "mart_customer_analysis.csv",
    "mart_product_performance.csv",
    "mart_monthly_revenue.csv",
]:
    shutil.copy2(src/name, dst/name)

print("Power BI files exported to powerbi_data/")
