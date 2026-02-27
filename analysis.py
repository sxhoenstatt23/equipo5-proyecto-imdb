#Cargamos nuestro archivo CSV
df = pd.read_csv("peliculas.csv")
# Eliminamos filas con datos nulos importantes
df = df.dropna(subset=["titulo", "anio", "genero", "calificacion", "votos"])
df.head()
