from pyspark.sql.functions import when, col
from config import SILVER_PATH, SURGE_PATH
from utils.helpers import ensure_dir


def run_surge_detection(spark):
    return flagged
