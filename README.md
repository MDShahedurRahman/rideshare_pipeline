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

## 🚀 How to Run

### 1️⃣ Install Dependencies

pip install -r requirements.txt

### 2️⃣ Run the Pipeline

python main.py

Pipeline will execute:

-   Bronze ingestion\
-   Silver transformation\
-   Surge detection\
-   Gold modeling\
-   KPI generation

------------------------------------------------------------------------

## 📊 Business KPIs Generated

-   Total revenue by payment method\
-   Surge ride identification\
-   Driver-level and rider-level dimensional modeling

Reports are saved in:

output/reports/

------------------------------------------------------------------------

## 🧠 Data Model (Gold Layer)

### Dimension Tables

dim_driver\
- driver_id\
- driver_name\
- city

dim_rider\
- rider_id

### Fact Table

fact_trips\
- trip_id\
- driver_id\
- rider_id\
- distance_km\
- duration_min\
- fare_amount\
- avg_speed_kmh\
- trip_date\
- payment_method\
- surge_flag

------------------------------------------------------------------------

## 🔥 Why This Project Matters

This project demonstrates:

-   Layered Data Lake architecture\
-   Star schema modeling\
-   Data quality transformations\
-   Business KPI generation\
-   Modular PySpark job design\
-   Clean project structure for production readiness

It reflects patterns used in real ride-sharing and mobility data
platforms.

------------------------------------------------------------------------
