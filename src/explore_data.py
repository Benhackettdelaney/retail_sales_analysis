
from pathlib import Path
import pandas as pd

# Find the dataset relative to this Python file
project_root = Path(__file__).resolve().parent.parent
file_path = project_root / "data" / "raw" / "Online Retail.xlsx"

# Load the Excel dataset
df = pd.read_excel(file_path)

# Display the first five rows
print("\nFIRST FIVE ROWS:")
print(df.head())

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Display column information
print("\nCOLUMN INFORMATION:")
df.info()

# Check for missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())
