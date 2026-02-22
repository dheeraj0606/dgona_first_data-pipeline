import pandas as pd
import sys

print("Running data validation...")

df = pd.read_csv("data/processed/orders_final.csv")

# Checks
errors = []

if df["quantity"].isnull().any():
    errors.append("Null values found in quantity")

if (df["quantity"] <= 0).any():
    errors.append("Invalid quantity values")

if df["price"].isnull().any():
    errors.append("Null values found in price")

if (df["price"] < 0).any():
    errors.append("Negative price values found")

# Result
if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("Validation passed!")

