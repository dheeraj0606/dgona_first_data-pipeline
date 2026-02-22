import pandas as pd

df = pd.read_csv("data/processed/orders_preview.csv")

print("Total Revenue:")
df["revenue"] = df["quantity"] * df["price"]
print(df["revenue"].sum())
s
print("\nRevenue by product:")
print(df.groupby("product")["revenue"].sum())
