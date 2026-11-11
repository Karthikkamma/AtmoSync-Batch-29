from pathlib import Path
import pandas as pd

# Find the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Existing agricultural price dataset
DATA_FILE = PROJECT_DIR / "dataset" / "raw" / "dataset.csv"

REQUIRED_COLUMNS = [
    "State",
    "District",
    "Market",
    "Commodity",
    "Arrival_Date",
    "Modal_x0020_Price"
]

def load_dataset():
    if not DATA_FILE.exists():
        print("ERROR: Dataset file not found!")
        print("Expected location:", DATA_FILE)
        return

    df = pd.read_csv(DATA_FILE)

    missing = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing:
        print("Missing columns:", missing)
        return

    df["Arrival_Date"] = pd.to_datetime(
        df["Arrival_Date"],
        dayfirst=True,
        errors="coerce"
    )

    print("\nDATASET INGESTION CHECK")
    print("-----------------------")
    print("Total records:", len(df))
    print("Valid dates:", df["Arrival_Date"].notna().sum())
    print("Unique dates:", df["Arrival_Date"].dt.date.nunique())
    print("Total commodities:", df["Commodity"].nunique())
    print("Total markets:", df["Market"].nunique())

    print("\nFirst 5 records:")
    print(df.head().to_string(index=False))

    print("\nDataset successfully loaded and validated.")

if __name__ == "__main__":
    load_dataset()