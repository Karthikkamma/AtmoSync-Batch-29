from pathlib import Path
import pandas as pd

project = Path(__file__).resolve().parent.parent

file = project / "dataset" / "processed" / "cleaned_dataset.csv"

df = pd.read_csv(file)

df["Arrival_Date"] = pd.to_datetime(
    df["Arrival_Date"],
    errors="coerce"
)

print("\nATMOSYNC DATA COVERAGE REPORT")

print("\nTotal records:", len(df))

print("\nEarliest date:", df["Arrival_Date"].min())
print("Latest date:", df["Arrival_Date"].max())

print("\nTotal states:", df["State"].nunique())
print("Total districts:", df["District"].nunique())
print("Total markets:", df["Market"].nunique())
print("Total commodities:", df["Commodity"].nunique())

print("\nTop 10 states by record count:")
print(df["State"].value_counts().head(10))

print("\nTop 10 commodities by record count:")
print(df["Commodity"].value_counts().head(10))

print("\nRecords by date:")
print(
    df.groupby(df["Arrival_Date"].dt.date)
    .size()
    .tail(10)
)