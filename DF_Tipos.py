
import pandas as pd

# Filas y columnas para df

columnas = ["Nombre", "Apellido", "Edad"]
fila_1 = ["Juliana", "Perez", 17]
fila_2 = ["Perla", "Ramirez", 28]

# Listas para df

nombres = ["Julia", "Pedro", "Juaquin"]
apellidos = ["De La Cruz", "Ramos", "Mercedez"]
edades = [44, 25, 39]

# Diccionario para df

diccionario = {
	"Nombres": nombres,
	"Apellidos": apellidos,
	"Edades": edades
}

# Creacion de los df

df_1 = pd.DataFrame([fila_1, fila_2], columns = columnas)
df_2 = pd.DataFrame(diccionario)

# Zip

df_3 = pd.DataFrame(list(zip(nombres, apellidos, edades)), columns = columnas)

# Mostrar datos

print(f"A partir de listas: \n{df_1}")
print(f"\nDiccionario: \n{df_2}")
print(f"\nZip: \n{df_3}")