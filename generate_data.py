from pathlib import Path
import random
from datetime import datetime, timedelta
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUT = PROJECT_ROOT / "data" / "raw"
OUT.mkdir(parents=True, exist_ok=True)

random.seed(42)

first_names = ["Ava","Noah","Mia","Liam","Emma","Ethan","Sophia","Lucas","Olivia","Mason","Isabella","James"]
last_names = ["Patel","Smith","Johnson","Brown","Garcia","Lee","Miller","Davis","Wilson","Anderson","Taylor","Thomas"]
states = ["GA","VA","TX","MO","IA","NC","FL","IL","CA","NY","NJ","PA"]
cities = {
    "GA":["Atlanta","Savannah"],
    "VA":["Norfolk","Richmond"],
    "TX":["Dallas","Austin"],
    "MO":["St. Louis","Kansas City"],
    "IA":["Des Moines","Cedar Rapids"],
    "NC":["Charlotte","Raleigh"],
    "FL":["Miami","Orlando"],
    "IL":["Chicago","Springfield"],
    "CA":["Los Angeles","San Diego"],
    "NY":["New York","Buffalo"],
    "NJ":["Newark","Jersey City"],
    "PA":["Philadelphia","Pittsburgh"],
}
category_map = {
    "Electronics":["Headphones","Keyboard","Mouse","Smart Watch","Speaker"],
    "Home":["Lamp","Storage Box","Cookware","Pillow","Desk"],
    "Beauty":["Skin Care","Hair Care","Fragrance","Makeup","Body Care"],
    "Fitness":["Yoga Mat","Dumbbells","Resistance Band","Bottle","Tracker"],
    "Grocery":["Snacks","Coffee","Tea","Protein Bar","Cereal"],
}
statuses = ["completed","shipped","processing","cancelled","refunded"]
status_weights = [0.60,0.20,0.10,0.06,0.04]
payment_methods = ["Credit Card","Debit Card","PayPal","Apple Pay","Google Pay"]

# Customers
customers=[]
for i in range(1,5001):
    state = random.choice(states)
    first = random.choice(first_names)
    last = random.choice(last_names)
    customers.append({
        "customer_id": f"C{i:06d}",
        "first_name": first,
        "last_name": last,
        "email": f"{first.lower()}.{last.lower()}{i}@example.com",
        "state": state,
        "city": random.choice(cities[state]),
        "signup_date": (datetime(2024,1,1)+timedelta(days=random.randint(0,900))).date().isoformat()
    })
pd.DataFrame(customers).to_csv(OUT/"customers.csv", index=False)

# Products
products=[]
product_id=1
for category, subs in category_map.items():
    for _ in range(20):
        sub=random.choice(subs)
        cost=round(random.uniform(4,180),2)
        price=round(cost*random.uniform(1.25,2.2),2)
        products.append({
            "product_id": f"P{product_id:05d}",
            "product_name": f"{sub} {product_id}",
            "category": category,
            "subcategory": sub,
            "unit_cost": cost,
            "list_price": price
        })
        product_id += 1
products_df=pd.DataFrame(products)
products_df.to_csv(OUT/"products.csv", index=False)

# Orders + items
orders=[]
items=[]
payments=[]
order_start=datetime(2025,1,1,8,0,0)
item_counter=1
payment_counter=1

for i in range(1,20001):
    customer_id=f"C{random.randint(1,5000):06d}"
    status=random.choices(statuses,weights=status_weights,k=1)[0]
    ts=order_start+timedelta(days=random.randint(0,620),hours=random.randint(0,14),minutes=random.randint(0,59))
    order_id=f"O{i:07d}"
    orders.append({
        "order_id":order_id,
        "customer_id":customer_id,
        "order_status":status,
        "order_timestamp":ts.isoformat(),
        "shipping_fee":round(random.uniform(0,14.99),2)
    })

    n_items=random.randint(1,4)
    selected = products_df.sample(n=n_items, replace=False, random_state=i)
    total=0.0
    for _, p in selected.iterrows():
        qty=random.randint(1,4)
        unit_price=float(p["list_price"])
        gross=qty*unit_price
        discount=round(gross*random.choice([0,0,0,0.05,0.10,0.15]),2)
        total += gross-discount
        items.append({
            "order_item_id":f"OI{item_counter:08d}",
            "order_id":order_id,
            "product_id":p["product_id"],
            "quantity":qty,
            "unit_price":unit_price,
            "discount_amount":discount
        })
        item_counter+=1

    payments.append({
        "payment_id":f"PAY{payment_counter:07d}",
        "order_id":order_id,
        "payment_method":random.choice(payment_methods),
        "payment_amount":round(total,2),
        "payment_timestamp":(ts+timedelta(minutes=random.randint(1,15))).isoformat()
    })
    payment_counter += 1

pd.DataFrame(orders).to_csv(OUT/"orders.csv", index=False)
pd.DataFrame(items).to_csv(OUT/"order_items.csv", index=False)
pd.DataFrame(payments).to_csv(OUT/"payments.csv", index=False)

print(f"Generated {len(customers):,} customers")
print(f"Generated {len(products):,} products")
print(f"Generated {len(orders):,} orders")
print(f"Generated {len(items):,} order items")
print(f"Generated {len(payments):,} payments")
