import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)
random.seed(42)

N = 50000  # number of transactions

# product catalog
n_products = 300
categories = ["Electronics","Home","Clothing","Food","Beauty","Sports"]
products = []
for i in range(n_products):
    products.append({
        "product_id": f"P{i+1:04d}",
        "product_name": f"Product_{i+1}",
        "category": random.choice(categories),
        "unit_price": round(np.random.uniform(50, 3000), 2)
    })
prod_df = pd.DataFrame(products)

# customers
n_customers = 8000
customers = [f"C{1000+i}" for i in range(n_customers)]

# transactions
rows = []
start = pd.to_datetime("2023-01-01")
end = pd.to_datetime("2024-12-31")
date_range_days = (end - start).days

for i in range(N):
    invoice = f"I{100000 + i}"
    order_date = start + pd.Timedelta(days=int(np.random.rand()*date_range_days),
                                      seconds=int(np.random.rand()*86400))
    cust = random.choice(customers)
    prod = prod_df.sample(1).iloc[0]
    qty = np.random.poisson(2)
    qty = max(1, qty)
    if np.random.rand() < 0.015:  # returns
        qty = -1 * random.choice([1,1,2])
    unit_price = prod.unit_price
    revenue = qty * unit_price
    rows.append({
        "InvoiceNo": invoice,
        "OrderDate": order_date,
        "CustomerID": cust,
        "ProductID": prod.product_id,
        "ProductName": prod.product_name,
        "Category": prod.category,
        "Quantity": qty,
        "UnitPrice": unit_price,
        "Revenue": round(revenue,2)
    })

df = pd.DataFrame(rows)
df.to_csv("data/retail_sales.csv", index=False)
print("Saved data/retail_sales.csv with", len(df), "rows")
