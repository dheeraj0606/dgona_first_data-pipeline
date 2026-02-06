import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/orders_preview.csv")

# Create revenue column
df["revenue"] = df["quantity"] * df["price"]

print("\nDataset with Revenue:")
print(df)

# Basic metrics
total_revenue = df["revenue"].sum()
total_orders = df["order_id"].count()
top_product = df.groupby("product")["revenue"].sum().idxmax()

print("\n📊 Business Metrics:")
print(f"Total Revenue: ${total_revenue}")
print(f"Total Orders: {total_orders}")
print(f"Top Product by Revenue: {top_product}")
