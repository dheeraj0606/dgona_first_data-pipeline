import pandas as pd
from config.config import PROCESSED_PATH, FINAL_OUTPUT_PATH

# Load cleaned data
#df = pd.read_csv("data/processed/orders_preview.csv")
df = pd.read_csv(PROCESSED_PATH)

df.to_csv(FINAL_OUTPUT_PATH, index=False)

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


def compute_metrics(file_path):
    df = pd.read_csv(file_path)

    return {
        "total_rows": len(df),
        "total_quantity": df["quantity"].sum(),
        "avg_price": df["price"].mean()
    }

if __name__ == "__main__":
    metrics = compute_metrics("../data/processed/orders_final.csv")
    print(metrics)
