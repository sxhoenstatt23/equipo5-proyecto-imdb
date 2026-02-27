#Grafica extra sobre la cantidad de peliculas estrenadas ese anio en el genero de terror
conteo = df_genero.groupby("anio")["calificacion"].count()
plt.figure()
conteo.plot(kind="bar")
plt.title("Cantidad de películas por año (Género: Terror)")
plt.xlabel("Año")
plt.ylabel("Número de películas")
plt.show()
