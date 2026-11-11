# AtmoSync – Dataset Sources

## 1. Agricultural Commodity Price Dataset

**Source:** AGMARKNET / data.gov.in (to be confirmed against the downloaded file)

**Purpose:** Analyze agricultural commodity prices across markets.

**Available fields:**
- State, District, Market
- Commodity, Variety, Grade
- Arrival Date
- Minimum, Maximum and Modal Prices

**Current coverage:**
- 12,672 records in the original dataset
- 10 November 2026 only

**Limitation:** Historical price data covering multiple dates is required.

## 2. Historical Weather Dataset

**Proposed source:** NASA POWER

**Website:** https://power.larc.nasa.gov/data-access-viewer/

**Required variables:**
- Temperature
- Relative humidity
- Precipitation

**Status:** Not yet downloaded.

## 3. Data Integration Plan

The datasets will be matched using dates and geographic locations.

Historical market prices and outdoor weather data will support exploratory climate-price analysis. They do not directly measure shipping-container conditions or actual spoilage.

## 4. Next Steps

- Obtain historical commodity-price records.
- Download historical weather data for matching locations and dates.
- Validate the datasets before integrating them into the ingestion pipeline.