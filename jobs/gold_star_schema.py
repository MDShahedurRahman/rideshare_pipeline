from config import SURGE_PATH, GOLD_PATH
from utils.helpers import ensure_dir


def run_gold_job(spark):
    print("Running Gold Layer...")

    ensure_dir(GOLD_PATH)

    df = spark.read.parquet(SURGE_PATH)

    dim_driver = df.select(
        "driver_id", "driver_name", "city"
    ).dropDuplicates()

    dim_rider = df.select(
        "rider_id"
    ).dropDuplicates()

    fact_trips = df.select(
        "trip_id",
        "driver_id",
        "rider_id",
        "distance_km",
        "duration_min",
        "fare_amount",
        "avg_speed_kmh",
        "trip_date",
        "payment_method",
        "surge_flag"
    )
