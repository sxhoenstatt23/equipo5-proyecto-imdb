# NGLC 27/02/2026
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datosPeliculas.csv") # Cargar los datos desde el archivo CSV
df = df.dropna(subset=["año", "titulo", "genero", "calificacion"])# Eliminar filas con datos faltantes en las columnas relevantes
genero = "comedia"
df_genero = df[df["genero"].str.contains(genero)]
promedio_por_año = df_genero.groupby("año")["calificacion"].mean()
plt.figure()
promedio_por_año.plot()# Graficar el promedio de calificación por año para el género seleccionado
plt.title("Promedio de calificación por año (Género: comedia)")
plt.xlabel("Año")
plt.ylabel("Calificación promedio")
plt.show()