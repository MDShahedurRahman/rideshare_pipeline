from pyspark.sql.functions import col, to_date
from config import BRONZE_PATH, SILVER_PATH
from utils.helpers import ensure_dir


def run_silver_job(spark):
    print("Running Silver Transformation...")

    ensure_dir(SILVER_PATH)

    df = spark.read.parquet(BRONZE_PATH)

    transformed = (
        df.dropDuplicates(["trip_id"])
    )

    return transformed
