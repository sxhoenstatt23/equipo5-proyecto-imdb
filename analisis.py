# Archivo: analisis.py
# Co-autores: Natalie (NGLC) y Rolando Garcia (RG)
# Fecha de modificación: 27/02/2026
# Descripción: Análisis de películas filtradas por género (Resolución de conflicto)

import pandas as pd
import matplotlib.pyplot as plt

# RG/NGLC - 27/02/2026 
# Cargamos los datos desde el archivo CSV
df = pd.read_csv("datosPeliculas.csv") 

# NGLC - Eliminamos filas con datos faltantes para evitar errores
# RG - Esto asegura que el análisis sea preciso
df = df.dropna(subset=["titulo", "anio", "genero", "calificacion"])

# Filtramos por género (Se puede cambiar a 'comedia' o 'Terror')
genero = "comedia"
df_genero = df[df["genero"].str.contains(genero, case=False)]

# Agrupamos por año y calculamos el promedio
promedio_por_año = df_genero.groupby("anio")["calificacion"].mean()

# Generación de la gráfica
promedio_por_año.plot()

plt.title(f"Promedio de calificación por año (Género: {genero})")
plt.xlabel("Año")
plt.ylabel("Calificación promedio")

# Firma de resolución de conflicto: Schoenstatt Olalde
plt.show()