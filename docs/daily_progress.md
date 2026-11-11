# AtmoSync Daily Progress

## Day 1

### Completed
- Created GitHub repository
- Added team members
- Created project folder structure
- Updated README

### Next Tasks
- Obtain the official dataset
- Inspect dataset columns
- Begin data cleaning
## 10 November 2026 – Daily Progress

**Project:** AtmoSync – Micro-Climate Arbitrage Analytics

### Work Completed
- Collected and inspected agricultural commodity price data.
- Cleaned and processed 12,672 records.
- Performed preliminary market price-difference analysis.
- Generated a visualization of the top 10 price differences.
- Checked dataset coverage using Python.
- Downloaded and validated an additional dataset.

### Findings
Both datasets contain records for only 10 November 2026. Historical data covering multiple dates is needed for further analysis.

### Next Steps
- Collect historical agricultural market price data.
- Integrate matching historical weather data.
## 11 November 2026 – Day 2 Progress

**Project:** AtmoSync – Micro-Climate Arbitrage Analytics

### Work Completed
- Documented the agricultural price dataset source and proposed historical weather dataset.
- Created the proposed data ingestion architecture.
- Developed `dataset_loader.py` to load and validate agricultural commodity price data.
- Validated 12,672 records covering 208 commodities and 1,301 markets.
- Developed `prepare_ingestion.py` to convert CSV records into JSONL format.
- Verified that the generated JSONL file contains 12,672 records.

### Findings
- All 12,672 records have valid dates.
- The available dataset covers only one date.
- JSONL records are prepared for future Kafka ingestion.

### Pending Work
- Obtain historical datasets covering multiple dates.
- Configure Kafka and Snowflake.
- Set up Apache Superset.

### Status
Python dataset ingestion preparation and validation completed. Kafka, Snowflake and Superset integration remain pending.