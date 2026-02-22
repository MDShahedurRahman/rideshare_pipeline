from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType,
    DoubleType
)


def trip_schema():
    return StructType([
        StructField("trip_id", IntegerType(), True),
        StructField("driver_id", StringType(), True),
        StructField("driver_name", StringType(), True),
        StructField("rider_id", StringType(), True),
        StructField("city", StringType(), True),
        StructField("distance_km", DoubleType(), True),
        StructField("duration_min", DoubleType(), True),
        StructField("fare_amount", DoubleType(), True),
        StructField("trip_date", StringType(), True),
        StructField("payment_method", StringType(), True)
    ])
