
from pathlib import Path
import pandas as pd

# Project paths
project_root = Path(__file__).resolve().parent.parent
input_file = project_root / "data/raw/Online Retail.xlsx"
output_dir = project_root / "data/processed"

output_dir.mkdir(parents=True, exist_ok=True)

# Load the original data
df = pd.read_excel(input_file)

print("Original rows:", len(df))

# Remove exact duplicates
df = df.drop_duplicates().copy()
print("After removing duplicates:", len(df))

# Standardise product descriptions
df["Description"] = (
    df["Description"]
    .astype("string")
    .str.strip()
)

# Convert customer IDs to nullable integers
df["CustomerID"] = df["CustomerID"].astype("Int64")

# Identify cancellations and returns
cancelled = (
    df["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
)

negative_quantity = df["Quantity"] < 0

# Preserve returns and cancellations separately
returns = df[cancelled | negative_quantity].copy()

returns.to_csv(
    output_dir / "returns_and_cancellations.csv",
    index=False
)

# Keep completed sales only
sales = df[
    (~cancelled)
    & (df["Quantity"] > 0)
    & (df["UnitPrice"] > 0)
    & (df["Description"].notna())
    & (df["Description"] != "")
].copy()

# Calculate revenue for each line item
sales["TotalPrice"] = (
    sales["Quantity"] * sales["UnitPrice"]
).round(2)

# Add useful date columns
sales["Year"] = sales["InvoiceDate"].dt.year
sales["Month"] = sales["InvoiceDate"].dt.month
sales["YearMonth"] = (
    sales["InvoiceDate"].dt.strftime("%Y-%m")
)

# Save the cleaned sales dataset
sales.to_csv(
    output_dir / "cleaned_sales.csv",
    index=False
)

# Summary
print("\nCLEANING SUMMARY")
print("-------------------------")
print("Clean sales rows:", len(sales))
print("Returns/cancellations:", len(returns))
print("Missing CustomerIDs in sales:",
      sales["CustomerID"].isna().sum())

print("\nTotal sales revenue: £",
      round(sales["TotalPrice"].sum(), 2))

print("\nFiles saved successfully!")
