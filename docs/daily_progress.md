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


## Day 3 — November 12, 2026

### Objective
Set up Apache Kafka and demonstrate agricultural price data ingestion.

### Work Completed
- Installed WSL2 with Ubuntu 24.04.
- Installed and configured Docker Desktop.
- Created a Docker Compose configuration for Apache Kafka 3.9.1.
- Started the Kafka broker in Docker.
- Created the `atmosync-prices` Kafka topic.
- Installed the `kafka-python` library.
- Developed `src/kafka_producer.py` to publish JSONL records.
- Published 12,672 agricultural market price records to Kafka.
- Verified Kafka topic offsets and successfully consumed three JSON messages.

### Files Created
- `docker-compose.yml`
- `src/kafka_producer.py`

### Result
Successfully demonstrated a local Kafka ingestion pipeline using public agricultural commodity price data.

### Limitations and Next Steps
- The current dataset contains prices from one date, not historical time-series data.
- Container IoT sensor simulation and Snowflake ingestion are not yet implemented.
- Next: build the simulated container telemetry producer and connect the Kafka pipeline to Snowflake.


## Day 4 - November 13, 2026

### Task: IoT Container Telemetry Simulation

- Started the Apache Kafka broker using Docker Compose.
- Created a new Kafka topic named `atmosync-telemetry`.
- Developed `src/iot_simulator.py` using Python.
- Simulated temperature, humidity, and GPS readings for three refrigerated containers.
- Added timestamps and a `simulated` flag to distinguish synthetic data from real sensor measurements.
- Published 15 simulated IoT readings to Apache Kafka.
- Verified Kafka ingestion by consuming 3 messages successfully.

### Result

Successfully implemented and tested the simulated IoT telemetry producer for AtmoSync.

### Next Steps

- Integrate Kafka telemetry streams with Snowflake.
- Create raw telemetry tables for downstream analytics.

