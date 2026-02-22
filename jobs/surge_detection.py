from pyspark.sql.functions import when, col
from config import SILVER_PATH, SURGE_PATH
from utils.helpers import ensure_dir


def run_surge_detection(spark):
    print("Running Surge Detection...")

    ensure_dir(SURGE_PATH)

    df = spark.read.parquet(SILVER_PATH)

    flagged = df.withColumn(
        "surge_flag",
        when(col("fare_amount") > 100, "HIGH_SURGE")
        .otherwise("NORMAL")
    )

    flagged.write.mode("overwrite").parquet(SURGE_PATH)

    print("Surge Detection Completed.")
    return flagged
