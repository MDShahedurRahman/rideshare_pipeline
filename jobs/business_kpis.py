from pyspark.sql.functions import sum, desc
from config import GOLD_PATH, REPORT_PATH
from utils.helpers import ensure_dir


def run_kpi_job(spark):
    print("Generating Business KPIs...")

    ensure_dir(REPORT_PATH)

    fact = spark.read.parquet(GOLD_PATH + "fact_trips/")

    revenue_by_city = (
        fact.groupBy("payment_method")
        .agg(sum("fare_amount").alias("total_revenue"))
        .orderBy(desc("total_revenue"))
    )

    revenue_by_city.show()

    revenue_by_city.write.mode("overwrite").csv(
        REPORT_PATH + "revenue_by_payment/",
        header=True
    )
