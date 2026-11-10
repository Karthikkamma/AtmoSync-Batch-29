from pathlib import Path
import pandas as pd

project = Path(__file__).resolve().parent.parent

file = project / "dataset" / "processed" / "cleaned_dataset.csv"

df = pd.read_csv(file)

# Ensure date and price are valid
df["Arrival_Date"] = pd.to_datetime(
    df["Arrival_Date"], errors="coerce"
)

df["Modal_Price"] = pd.to_numeric(
    df["Modal_Price"], errors="coerce"
)

df = df.dropna(
    subset=["Arrival_Date", "Commodity", "Market", "Modal_Price"]
)

# Compare prices only within the same date and commodity
results = []

for (date, commodity, variety, grade), group in df.groupby(
    ["Arrival_Date", "Commodity", "Variety", "Grade"],
    dropna=False
):
    if group["Market"].nunique() < 2:
        continue

    cheapest = group.loc[group["Modal_Price"].idxmin()]
    expensive = group.loc[group["Modal_Price"].idxmax()]

    difference = expensive["Modal_Price"] - cheapest["Modal_Price"]

    if difference <= 0:
        continue

    results.append({"Variety": variety,
"Grade": grade,
    })

result_df = pd.DataFrame(results)

output = project / "dataset" / "processed" / "price_opportunities.csv"

result_df.to_csv(output, index=False)

print("\nTotal price opportunities:", len(result_df))

if not result_df.empty:
    print("\nTop 10 price differences:")
    print(
        result_df.sort_values(
            "Price_Difference", ascending=False
        ).head(10).to_string(index=False)
    )

print("\nSaved:", output)