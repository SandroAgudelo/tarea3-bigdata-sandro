# Tarea 3 - Procesamiento de Datos con Apache Spark

Estudiante: Sandro Augusto Agudelo Parra  
Curso: Big Data  
Código: 202016911  
Grupo: 37  

## Descripción

Este repositorio contiene el desarrollo individual de la Tarea 3, relacionado con procesamiento batch mediante Apache Spark y análisis de datos en tiempo real utilizando Apache Kafka y Spark Streaming.

## Archivos

- spark_batch_taxi.py
- kafka_producer.py
- spark_streaming_consumer.py
- graficas_taxi.py

## Procesamiento batch

Se utilizó el conjunto de datos NYC TLC Yellow Taxi Trip Records para realizar:

- Carga de datos.
- Limpieza de registros.
- Transformación de variables.
- Análisis exploratorio.
- Viajes por hora.
- Distancia promedio.
- Tarifa promedio.
- Generación de gráficas.

## Procesamiento en tiempo real

Se utilizó Apache Kafka con el topic sensor_data.

El productor genera datos simulados de temperatura y humedad, mientras que Spark Streaming consume los registros y calcula estadísticas por sensor.
