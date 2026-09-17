from pathlib import Path
import sys, subprocess
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.quality import (
    validate_customers, validate_products, validate_orders,
    validate_order_items, validate_payments, raise_if_errors,
)
from src.transformations import (
    clean_customers, clean_products, clean_orders, clean_order_items, clean_payments,
    build_order_detail, build_sales_summary, build_customer_analysis,
    build_product_performance, build_monthly_revenue,
)

RAW = PROJECT_ROOT/"data"/"raw"
OUT = PROJECT_ROOT/"data"/"processed"
OUT.mkdir(parents=True, exist_ok=True)

if not (RAW/"orders.csv").exists():
    subprocess.check_call([sys.executable, str(PROJECT_ROOT/"scripts"/"generate_data.py")])

customers=clean_customers(pd.read_csv(RAW/"customers.csv"))
products=clean_products(pd.read_csv(RAW/"products.csv"))
orders=clean_orders(pd.read_csv(RAW/"orders.csv"))
items=clean_order_items(pd.read_csv(RAW/"order_items.csv"))
payments=clean_payments(pd.read_csv(RAW/"payments.csv"))

raise_if_errors("customers", validate_customers(customers))
raise_if_errors("products", validate_products(products))
raise_if_errors("orders", validate_orders(orders))
raise_if_errors("order_items", validate_order_items(items))
raise_if_errors("payments", validate_payments(payments))

detail=build_order_detail(orders,items,products,customers)
sales=build_sales_summary(detail)
customers_mart=build_customer_analysis(detail)
products_mart=build_product_performance(detail)
monthly=build_monthly_revenue(detail)

detail.to_csv(OUT/"order_detail.csv", index=False)
sales.to_csv(OUT/"mart_sales_summary.csv", index=False)
customers_mart.to_csv(OUT/"mart_customer_analysis.csv", index=False)
products_mart.to_csv(OUT/"mart_product_performance.csv", index=False)
monthly.to_csv(OUT/"mart_monthly_revenue.csv", index=False)

valid=detail[~detail["order_status"].isin(["cancelled","refunded"])]
print("Pipeline completed successfully.")
print(f"Orders: {orders['order_id'].nunique():,}")
print(f"Order items: {len(items):,}")
print(f"Customers: {customers['customer_id'].nunique():,}")
print(f"Revenue: ${valid['net_sales'].sum():,.2f}")
print(f"Profit: ${valid['profit'].sum():,.2f}")
