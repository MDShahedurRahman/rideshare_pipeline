from pyspark.sql.functions import when, col
from config import SILVER_PATH, SURGE_PATH
from utils.helpers import ensure_dir


def run_surge_detection(spark):
    print("Running Surge Detection...")

    ensure_dir(SURGE_PATH)

    df = spark.read.parquet(SILVER_PATH)

    flagged = df.withColumn(
        "surge_flag"
    )

    return flagged
