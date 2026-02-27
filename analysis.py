#Cargamos nuestro archivo CSV
df = pd.read_csv("datosPeliculas.csv")
# Eliminamos filas con datos nulos importantes
df = df.dropna(subset=["titulo", "anio", "genero", "calificacion", "votos"])
df.head()
#Filtramos por un genero en especifico
genero = "Terror"
df_genero = df[df["genero"].str.contains(genero)]
df_genero.head()
#Calculamos el promedio de la calificacion por anio de estas
promedio_por_año = df_genero.groupby("anio")["calificacion"].mean()
#Creamos una grafica para mostrar la anterior informacion
plt.figure()
promedio_por_año.plot()
plt.title("Promedio de calificación por año (Género: Terror)")
plt.xlabel("Año")
plt.ylabel("Calificación promedio")
plt.show()
