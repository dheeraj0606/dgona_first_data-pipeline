import pandas as pd
import logging
from config.config import RAW_DATA_PATH, PROCESSED_PATH

logging.basicConfig(level=logging.INFO)

logging.info("Reading raw data...")
df = pd.read_csv(RAW_DATA_PATH)

logging.info("Cleaning data...")
df = df.dropna()

df.to_csv(PROCESSED_PATH, index=False)

logging.info("Cleaned data saved!")

