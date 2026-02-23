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
