import os

print("Starting pipeline...")

print("Step 1: Cleaning data")
os.system("python3 scripts/clean.py")

print("Step 2: Calculating metrics")
os.system("python3 scripts/metrics.py")

print("Pipeline completed successfully!")

