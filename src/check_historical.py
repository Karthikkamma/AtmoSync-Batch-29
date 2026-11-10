from pathlib import Path
import pandas as pd

project = Path(__file__).resolve().parent.parent
file = project / "dataset" / "raw" / "historical_tomato.csv"

print("Looking for:", file)
print("File exists:", file.exists())

df = pd.read_csv(file)
df = pd.read_csv(file)

print("\nTotal rows:", len(df))
print("\nColumns:", df.columns.tolist())

date_col = "Arrival_Date"

if date_col in df.columns:
    dates = pd.to_datetime(
        df[date_col],
        dayfirst=True,
        errors="coerce"
    )

    print("\nEarliest date:", dates.min())
    print("Latest date:", dates.max())
    print("Unique dates:", dates.dt.date.nunique())
else:
    print("\nDate column not found")