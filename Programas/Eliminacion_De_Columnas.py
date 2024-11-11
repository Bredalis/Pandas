
import pandas as pd

# Cargar el DataFrame y mostar las primeras filas
df = pd.read_csv("../CSV/All_Bikez_Curated.csv") 
print(f"Primeras filas del DataFrame:\n{df.head()}")

print(f"\nTipos de datos en el DataFrame:\n{df.dtypes}")

# Eliminar columnas de tipo 'object' y mostrar el resultado
df = df.select_dtypes(exclude = ["object"])
print(f"\nDataFrame sin columnas de tipo 'object':\n{df}")