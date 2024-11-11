
import pandas as pd

# Diccionario de datos para crear el DataFrame
datos = {
    "Paises": ["RD", "Perú", "Brasil", "Colombia", "Venezuela"],
    "Capital": ["Santo Domingo", "Lima", "Brasilia", "Bogotá", "Caracas"],
    "Poblacion": [10000, 10000, 10000, 1000, 1000]
}

# Creación de DataFrames
df_1 = pd.DataFrame(datos)
df_2 = pd.DataFrame(datos, columns = ["Paises", "Poblacion"])
df_3 = pd.DataFrame(datos, index = datos["Paises"], columns = ["Capital", "Poblacion"])

# Mostrar datos de los DataFrames
print("DataFrame completo:\n", df_1)
print("\nEncabezado del DataFrame:\n", df_1.head())
print("\nÚltimas filas del DataFrame:\n", df_1.tail())
print("\nDataFrame (Posiciones 0 a 4):\n", df_1[0:4])

print("\nDataFrame 2 (Columnas 'Paises' y 'Poblacion'):\n", df_2)

print("\nDataFrame 3 (Indexado por países):\n", df_3)
print("\nColumna 'Poblacion' en DataFrame 3:\n", df_3["Poblacion"])

print("\nPoblación de RD y Perú en DataFrame 3 (usando loc):\n", df_3.loc[["RD", "Perú"], ["Poblacion"]])
print("\nPoblación de RD y Perú en DataFrame 3 (usando iloc):\n", df_3.iloc[[0, 1], [1]])