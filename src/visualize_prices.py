from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

project = Path(__file__).resolve().parent.parent

input_file = (
    project / "dataset" / "processed"
    / "price_opportunities.csv"
)

df = pd.read_csv(input_file)

if df.empty:
    print("No price opportunities available to plot.")
else:
    top10 = df.nlargest(10, "Price_Difference").copy()

    top10["Label"] = (
        top10["Commodity"].astype(str)
        + " | "
        + top10["Buy_Market"].astype(str)
        + " → "
        + top10["Sell_Market"].astype(str)
    )

    plt.figure(figsize=(12, 7))

    plt.barh(
        top10["Label"],
        top10["Price_Difference"]
    )

    plt.xlabel("Modal price difference (dataset price units)")
    plt.ylabel("Commodity and markets")
    plt.title("AtmoSync - Top 10 Market Price Differences")

    plt.gca().invert_yaxis()
    plt.tight_layout()

    output = (
        project / "reports" / "top10_price_differences.png"
    )

    output.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(output, dpi=150, bbox_inches="tight")

    print("Chart saved to:", output)