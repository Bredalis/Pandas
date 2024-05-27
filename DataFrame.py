
"""
Diferentes maneras 
de crear un df
"""

import pandas as pd

# Diccionario para df

datos = {
	"Nombre": ["Perla", "Pedro", "Pedrito"],
	"Edad": [23, 24, 25],
	"Pais": ["Puerto Rico", "RD", "Chile"]
}

# Creacion de los df

df_1 = pd.DataFrame(datos)
df_2 = pd.DataFrame({
	"Colores": ["Rojo", "Verde", "Azul", "Naranja"],
	"Puntuación": [5, 7, 9, 0]
})

# Mostrar datos

print(f"Tamaño: {df_1.shape}")
print(f"\nEncabezado: \n {df_1.head()}")
print(f"\nDescripcion: \n {df_1.describe()}")

print(f"\nDF 1: \n{df_1}")
print(f"\nDF 2: \n{df_2}")

# Cambiar nombres de columnas en df 2

df_2.columns = ["Colors", "Punctuation"]
print(f"\nDF 2: \n{df_2}")