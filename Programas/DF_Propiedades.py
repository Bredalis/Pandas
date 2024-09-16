
import pandas as pd

# Diccionario para df

datos = {
	"Paises": ["RD", "Peru", "Brasil", "Colombia", "Venezuela"],
	"Capital": ["Santo Domingo", "Lima", "Brasilia", "Bogota", "Caracas"],
	"Poblacion": [10000, 10000, 10000, 1000, 1000]
}

# Creacion de los df

df_1 = pd.DataFrame(datos)
df_2 = pd.DataFrame(datos, columns = ["Paises", "Poblacion"])
df_3 = pd.DataFrame(datos, index = [datos["Paises"]], 
	columns = ["Capital", "Poblacion"])

# Mostrar datos

print(f"DataFrame: \n{df_1}")
print(f"\nEncabezado: \n{df_1.head()}")
print(f"\nUltimas: \n{df_1.tail()}")

print(f"\nDF (Posicion 0 - 4): \n{df_1[0:4]}")
print(f"\nDF 2: \n{df_2}")

print(f"\nDF 3: \n{df_3}")
print(f"\nDF 3 (Poblacion):\n{df_3.Poblacion}")

print(f"\nDF 3 (Mostrar población de RD y Peru): \n", 
	df_3.loc[["RD", "Peru"], ["Poblacion"]])

print(f"\nDF 3 (Mostrar poblacion de RD y Peru): \n", 
	df_3.iloc[[0, 1], [1]])