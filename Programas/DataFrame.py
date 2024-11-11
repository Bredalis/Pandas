
import pandas as pd

# Diccionario de datos para crear el DataFrame
datos = {
	"Nombre": ["Perla", "Pedro", "Pedrito"],
	"Edad": [23, 24, 25],
	"Pais": ["Puerto Rico", "RD", "Chile"]
}

# Creación de DataFrame
df_1 = pd.DataFrame(datos)
df_2 = pd.DataFrame({
	"Colores": ["Rojo", "Verde", "Azul", "Naranja"],
	"Puntuacion": [5, 7, 9, 0]
})

# Mostrar información y contenido de los DataFrames
print(f"Tamaño de df_1: {df_1.shape}")
print(f"\nEncabezado de df_1:\n{df_1.head()}")
print(f"\nDescripción de df_1:\n{df_1.describe()}")
print(f"\nContenido de df_1:\n{df_1}")
print(f"\nContenido de df_2:\n{df_2}")

# Cambiar nombres de columnas en df_2
df_2.columns = ["Colors", "Punctuation"]
print(f"\nContenido actualizado de df_2:\n{df_2}")