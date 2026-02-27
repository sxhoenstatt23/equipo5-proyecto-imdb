# Archivo: analisis.py
# Autor: Rolando Garcia
# Fecha de modificación: 26/02/2026 11:23
# Descripción: Análisis de películas filtradas por género

import pandas as pd
import matplotlib.pyplot as plt

# RG - 26/02/2026 
# Cargamos el archivo CSV generado previamente con datos de películas
df = pd.read_csv("datosPeliculas.csv")

# RG - 26/02/2026
# Eliminamos filas que tengan valores nulos en columnas importantes
# Esto asegura que el análisis no tenga errores por datos faltantes
df = df.dropna(subset=["titulo", "anio", "genero", "calificacion"])

# RG - 26/02/2026
# Filtramos las películas por un género específico (en este caso "Terror")
# str.contains permite buscar coincidencias dentro del texto
genero = "Terror"
df_genero = df[df["genero"].str.contains(genero)]

# RG - 26/02/2026
# Agrupamos las películas por año y calculamos el promedio de calificación para cada año
promedio_por_año = df_genero.groupby("anio")["calificacion"].mean()

# RG - 26/02/2026
# Creamos una gráfica de línea para visualizar la evolución del promedio de calificación a lo largo del tiempo
plt.figure()
promedio_por_año.plot()

plt.title("Promedio de calificación por año (Género: Terror)")
plt.xlabel("Año")
plt.ylabel("Calificación promedio")

# Mostramos la gráfica en pantalla
plt.show()

#fin