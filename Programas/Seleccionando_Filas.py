
import pandas as pd

# Crear el DataFrame
df = pd.DataFrame({
    "Nombres": ["Yulissa", "Juanmy", "Lucas"],
    "Edad": [37, 25, 27],
    "DNI": ["480140", "40856", "48976"]
})

# Maneras de seleccionar filas de un DataFrame
print("Método para revisar si hay un determinado dato:\n", df.Nombres.isin(["Yulissa", "Perla"]))
print("\nSelección básica:\n", df[df["Nombres"] == "Lucas"])
print("\nSeleccionar por posición:\n", df.iloc[[0, 1], [0, 2]])

# Poner la columna 'Nombres' como índice
nombres_indexado = df.set_index("Nombres")

# Mostrar datos
print("\nDataFrame con 'Nombres' como índice:\n", nombres_indexado)
print("\nDataFrame original:\n", df)