from pyspark.sql.functions import sum, desc
from config import GOLD_PATH, REPORT_PATH
from utils.helpers import ensure_dir


def run_kpi_job(spark):
