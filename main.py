from utils.spark_session import get_spark_session

from jobs.bronze_ingestion import run_bronze_job
from jobs.silver_transformation import run_silver_job
from jobs.surge_detection import run_surge_detection
from jobs.gold_star_schema import run_gold_job
from jobs.business_kpis import run_kpi_job


def main():
    spark = get_spark_session()

    run_bronze_job(spark)
    run_silver_job(spark)
    run_surge_detection(spark)
    run_gold_job(spark)


if __name__ == "__main__":
    main()
