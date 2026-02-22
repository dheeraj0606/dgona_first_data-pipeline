import pandas as pd
from config.config import RAW_DATA_PATH, PROCESSED_PATH

df = pd.read_csv(RAW_DATA_PATH)

# Simple cleaning
df = df.dropna()
df["quantity"] = df["quantity"].astype(int)
df["price"] = df["price"].astype(float)

df.to_csv(PROCESSED_PATH, index=False)

print("Data cleaned and saved!")

