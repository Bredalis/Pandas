
import pandas as pd

# Cargar el DataFrame
datos = pd.read_csv("../CSV/Clientes.csv")

# Manejo de datos faltantes
print("Datos faltantes en la columna 'nombre':\n", datos["nombre"].isnull())
print("\nDatos sin valores faltantes:\n", datos.dropna())

# Eliminar filas con NaN en columnas específicas
datos.dropna(subset = ["nombre", "ingreso"], inplace = True)
print("\nDatos después de eliminar NaN en 'nombre' y 'ingreso':\n", datos)

# Valores para sustituir NaN
valores_para_sustituir = {
    "nombre": "Desconocido",
    "edad": 18,
    "ingreso": 10000
}

# Sustituir NaN en el DataFrame
print("\nDataFrame con NaN sustituidos:\n", datos.fillna(value = valores_para_sustituir))

# Mostrar estadísticas de la columna 'ingreso'
print("\nPromedio de ingreso:", datos["ingreso"].mean())
print("Mediana de ingreso:", datos["ingreso"].median())
print("Moda de ingreso:", datos["ingreso"].mode())