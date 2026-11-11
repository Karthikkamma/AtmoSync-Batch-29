from pathlib import Path
import json
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_DIR / "dataset" / "raw" / "dataset.csv"
OUTPUT_FILE = PROJECT_DIR / "dataset" / "processed" / "price_records.jsonl"

df = pd.read_csv(INPUT_FILE)

# Standardize column names
df.columns = df.columns.str.replace("_x0020_", "_", regex=False)

# Convert date to standard format
df["Arrival_Date"] = pd.to_datetime(
    df["Arrival_Date"],
    dayfirst=True,
    errors="coerce"
).dt.strftime("%Y-%m-%d")

# Create output directory if needed
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Save one JSON object per line
with OUTPUT_FILE.open("w", encoding="utf-8") as f:
    for record in df.to_dict(orient="records"):
        f.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")

print("JSONL preparation completed.")
print("Records prepared:", len(df))
print("Output file:", OUTPUT_FILE)
print("Actual output path:", OUTPUT_FILE.resolve())
print("File exists:", OUTPUT_FILE.exists())
with OUTPUT_FILE.open("r", encoding="utf-8") as f:
    line_count = sum(1 for line in f)

print("JSONL record count:", line_count)