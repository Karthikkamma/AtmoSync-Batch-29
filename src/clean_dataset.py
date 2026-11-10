from pathlib import Path
import pandas as pd

# Project folders
project = Path(__file__).resolve().parent.parent
input_file = project / "dataset" / "raw" / "dataset.csv"
output_folder = project / "dataset" / "processed"

output_folder.mkdir(parents=True, exist_ok=True)

# Read original dataset
df = pd.read_csv(input_file)

print("Original rows:", len(df))

# Clean column names
df.columns = (
    df.columns
    .str.replace("_x0020_", "_", regex=False)
    .str.strip()
)

# Convert date
df["Arrival_Date"] = pd.to_datetime(
    df["Arrival_Date"],
    dayfirst=True,
    errors="coerce"
)

# Convert prices to numbers
price_columns = [
    "Min_Price",
    "Max_Price",
    "Modal_Price"
]

for column in price_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

# Remove duplicate records
df = df.drop_duplicates()

# Save cleaned dataset
output_file = output_folder / "cleaned_dataset.csv"
df.to_csv(output_file, index=False)

print("Cleaned rows:", len(df))
print("Invalid dates:", df["Arrival_Date"].isna().sum())
print("Missing price values:")
print(df[price_columns].isna().sum())
print("Saved file:", output_file)