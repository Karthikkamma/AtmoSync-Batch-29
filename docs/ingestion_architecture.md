# AtmoSync – Proposed Data Ingestion Architecture

## Objective

Prepare a data pipeline for agricultural market prices and historical weather datasets, aligned with the Week 1 data engineering objectives.

## Proposed Pipeline

Public Agricultural Price Data + Historical Weather Data

↓

Python Data Loading and Validation

↓

Apache Kafka (Data Ingestion)

↓

Snowflake (Raw Data Storage)

↓

dbt (Data Cleaning and Transformation)

↓

Apache Superset (Analytics Dashboard)

## Component Responsibilities

**Python**
- Load CSV datasets.
- Validate dates, locations and required columns.
- Prepare records for ingestion.

**Apache Kafka**
- Receive dataset records as messages.
- Provide a streaming ingestion layer.

**Snowflake**
- Store ingested records in raw tables.
- Support historical analysis.

**dbt**
- Clean and transform raw records.
- Join price and weather data where dates and locations match.

**Apache Superset**
- Visualize market price differences and weather patterns.

## Current Status

- Agricultural price dataset collected and inspected.
- Initial price analysis completed.
- Historical price data still required.
- Weather data not yet collected.
- Kafka, Snowflake, dbt and Superset not yet configured.

## Important Limitation

This dataset-based pipeline supports market and outdoor-weather analysis. It does not directly measure container conditions or calculate validated spoilage rates without additional relevant data.