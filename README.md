# 🚗 Smart Ride-Sharing Data Engineering Pipeline (PySpark)

## 📌 Overview

This project simulates a real-world ride-sharing data platform similar
to Uber or Lyft.\
It demonstrates how raw trip-level data flows through a modern data
engineering architecture using PySpark and a layered Data Lake design
(Bronze → Silver → Gold).

The pipeline ingests trip data, performs cleaning and enrichment,
detects surge pricing scenarios, builds a star schema model, and
generates business KPIs.

This project is designed for data engineering portfolios and mirrors
production-style batch pipelines.

------------------------------------------------------------------------

## 🏗 Architecture

Raw CSV Data\
↓\
Bronze Layer (Raw Ingestion)\
↓\
Silver Layer (Cleaned + Enriched)\
↓\
Surge Detection Layer\
↓\
Gold Layer (Star Schema)\
↓\
Business KPI Reports

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3.9+
-   PySpark 3.5
-   Parquet (Data Lake format)
-   CSV (Raw data)
-   Local file system storage

------------------------------------------------------------------------

## 📂 Project Structure
```
rideshare_pipeline/

├── main.py\
├── config.py\
├── requirements.txt

├── data/\
│ └── trips.csv

├── jobs/\
│ ├── bronze_ingestion.py\
│ ├── silver_transformation.py\
│ ├── surge_detection.py\
│ ├── gold_star_schema.py\
│ └── business_kpis.py

├── utils/\
│ ├── spark_session.py\
│ ├── schema.py\
│ └── helpers.py

└── output/\
├── bronze/\
├── silver/\
├── gold/\
└── reports/
```
------------------------------------------------------------------------
