from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, avg, count, round

spark = SparkSession.builder \
    .appName("NYC_Taxi_Batch_Analysis") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Cargar dataset
df = spark.read.parquet("yellow_tripdata_2024-01.parquet")

print("\n===== ESQUEMA DEL DATASET =====")
df.printSchema()

print("\n===== PRIMEROS REGISTROS =====")
df.show(10, truncate=False)

print("\n===== TOTAL DE REGISTROS =====")
print("Total original:", df.count())

# Seleccionar variables principales
taxi_df = df.select(
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "passenger_count",
    "trip_distance",
    "fare_amount",
    "total_amount",
    "payment_type"
)

# Eliminar valores nulos
clean_df = taxi_df.dropna(
    subset=[
        "tpep_pickup_datetime",
        "trip_distance",
        "fare_amount",
        "total_amount"
    ]
)

# Eliminar registros inconsistentes
clean_df = clean_df.filter(
    (col("trip_distance") > 0) &
    (col("fare_amount") > 0) &
    (col("total_amount") > 0)
)

# Eliminar registros duplicados
clean_df = clean_df.dropDuplicates()

print("\n===== REGISTROS DESPUÉS DE LIMPIEZA =====")
print("Total limpio:", clean_df.count())

# Obtener hora del viaje
clean_df = clean_df.withColumn(
    "pickup_hour",
    hour(col("tpep_pickup_datetime"))
)

print("\n===== ESTADÍSTICAS GENERALES =====")
clean_df.select(
    "trip_distance",
    "fare_amount",
    "total_amount",
    "passenger_count"
).describe().show()

# Cantidad de viajes por hora
print("\n===== VIAJES POR HORA =====")

trips_by_hour = clean_df \
    .groupBy("pickup_hour") \
    .agg(count("*").alias("total_trips")) \
    .orderBy(col("total_trips").desc())

trips_by_hour.show(24)

# Distancia promedio
print("\n===== DISTANCIA PROMEDIO =====")

clean_df.select(
    round(avg("trip_distance"), 2).alias("average_trip_distance")
).show()

# Tarifa promedio
print("\n===== TARIFA PROMEDIO =====")

clean_df.select(
    round(avg("fare_amount"), 2).alias("average_fare")
).show()

# Valor total promedio
print("\n===== VALOR TOTAL PROMEDIO =====")

clean_df.select(
    round(avg("total_amount"), 2).alias("average_total_amount")
).show()

# Análisis por hora
print("\n===== ANÁLISIS POR HORA =====")

hour_analysis = clean_df \
    .groupBy("pickup_hour") \
    .agg(
        count("*").alias("total_trips"),
        round(avg("trip_distance"), 2).alias("avg_distance"),
        round(avg("fare_amount"), 2).alias("avg_fare")
    ) \
    .orderBy("pickup_hour")

hour_analysis.show(24)

# Guardar resultados
trips_by_hour.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("resultado_viajes_hora")

hour_analysis.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("resultado_analisis_hora")

print("\n===== PROCESAMIENTO FINALIZADO CORRECTAMENTE =====")

spark.stop()
