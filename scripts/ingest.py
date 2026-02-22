import pandas as pd

# Load raw CSV
orders = pd.read_csv("../data/raw/orders.csv")

# Preview data
print("Preview of orders dataset:")
print(orders.head())

# Optional: Save to processed folder
orders.to_csv("../data/processed/orders_preview.csv", index=False)
