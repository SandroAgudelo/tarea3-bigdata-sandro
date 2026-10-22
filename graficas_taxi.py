import glob
import pandas as pd
import matplotlib.pyplot as plt

archivo = glob.glob("resultado_analisis_hora/part-*.csv")[0]

df = pd.read_csv(archivo)

# Gráfica 1: cantidad de viajes por hora
plt.figure(figsize=(10, 5))
plt.bar(df["pickup_hour"], df["total_trips"])
plt.xlabel("Hora del día")
plt.ylabel("Cantidad de viajes")
plt.title("Cantidad de viajes por hora")
plt.xticks(range(24))
plt.tight_layout()
plt.savefig("viajes_por_hora.png")
plt.close()

# Gráfica 2: tarifa promedio por hora
plt.figure(figsize=(10, 5))
plt.plot(df["pickup_hour"], df["avg_fare"], marker="o")
plt.xlabel("Hora del día")
plt.ylabel("Tarifa promedio")
plt.title("Tarifa promedio por hora")
plt.xticks(range(24))
plt.tight_layout()
plt.savefig("tarifa_promedio_hora.png")
plt.close()

# Gráfica 3: distancia promedio por hora
plt.figure(figsize=(10, 5))
plt.plot(df["pickup_hour"], df["avg_distance"], marker="o")
plt.xlabel("Hora del día")
plt.ylabel("Distancia promedio")
plt.title("Distancia promedio por hora")
plt.xticks(range(24))
plt.tight_layout()
plt.savefig("distancia_promedio_hora.png")
plt.close()

print("Gráficas generadas correctamente.")
