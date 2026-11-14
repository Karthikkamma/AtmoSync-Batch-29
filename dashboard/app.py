
import streamlit as st
import pandas as pd
from pathlib import Path

# Configure dashboard
st.set_page_config(
    page_title="AtmoSync Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# Dashboard title
st.title("🌦️ AtmoSync – Micro-Climate Arbitrage Analytics")

st.write(
    "An interactive dashboard for agricultural market "
    "prices, container telemetry, and arbitrage opportunities."
)

# Project overview
st.header("📊 Project Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Agricultural Price Records", "12,672")

with col2:
    st.metric("Container Telemetry Records", "15")

with col3:
    st.metric("Data Platform", "Snowflake")

st.success("AtmoSync dashboard initialized successfully!")

# Agricultural market price data
st.header("🌾 Agricultural Market Price Data")

# Locate the dataset from the project root
project_root = Path(__file__).resolve().parent.parent
csv_path = project_root / "dataset" / "processed" / "cleaned_dataset.csv"

# Load agricultural market prices
df = pd.read_csv(csv_path)

# Display total records
st.write(f"Total agricultural price records: {len(df):,}")
# Interactive commodity filter
st.subheader("🔍 Filter by Commodity")

commodities = ["All Commodities"] + sorted(
    df["Commodity"].dropna().unique().tolist()
)

selected_commodity = st.selectbox(
    "Select a Commodity",
    commodities
)

if selected_commodity == "All Commodities":
    filtered_df = df
else:
    filtered_df = df[df["Commodity"] == selected_commodity]
    # Interactive market filter
st.subheader("🏪 Filter by Market")

markets = ["All Markets"] + sorted(
    filtered_df["Market"].dropna().unique().tolist()
)

selected_market = st.selectbox(
    "Select a Market",
    markets
)

if selected_market != "All Markets":
    filtered_df = filtered_df[
        filtered_df["Market"] == selected_market
    ]

# Display the first 20 records
st.dataframe(filtered_df.head(20), use_container_width=True)
# Agricultural market price comparison chart
st.header("📊 Agricultural Market Price Comparison")

if not filtered_df.empty:
    market_prices = (
        filtered_df.groupby("Market")["Modal_Price"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    st.subheader("Top 10 Markets by Average Modal Price")

    st.bar_chart(market_prices)

    st.caption(
        "Average modal prices for the selected commodity "
        "and market filters."
    )
else:
    st.warning("No price records found for the selected filters.")
# Agricultural price difference analysis
st.header("💰 Agricultural Price Difference Analysis")

if selected_commodity == "All Commodities":
    st.info("Select a specific commodity to analyze market price differences.")
else:
    commodity_data = df[df["Commodity"] == selected_commodity]

    market_avg = (
        commodity_data.groupby("Market")["Modal_Price"]
        .mean()
        .sort_values()
    )

    if len(market_avg) >= 2:
        lowest_market = market_avg.index[0]
        highest_market = market_avg.index[-1]

        lowest_price = market_avg.iloc[0]
        highest_price = market_avg.iloc[-1]
        price_difference = highest_price - lowest_price

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Lowest Average Price", f"₹{lowest_price:,.2f}")
            st.caption(lowest_market)

        with col2:
            st.metric("Highest Average Price", f"₹{highest_price:,.2f}")
            st.caption(highest_market)

        with col3:
            st.metric("Price Difference", f"₹{price_difference:,.2f}")

        st.info(
            "This price difference indicates a potential market arbitrage "
            "opportunity. Transportation costs and other expenses are not included."
        )
    else:
        st.warning(
            "At least two markets are required for price difference analysis."
        )