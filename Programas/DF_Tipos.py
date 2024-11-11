
import pandas as pd

# Definir columnas y filas
columnas = ["Nombre", "Apellido", "Edad"]
fila_1 = ["Juliana", "Pérez", 17]
fila_2 = ["Perla", "Ramírez", 28]

# Listas de datos
nombres = ["Julia", "Pedro", "Joaquín"]
apellidos = ["De La Cruz", "Ramos", "Mercedes"]
edades = [44, 25, 39]

# Crear DataFrames
df_1 = pd.DataFrame([fila_1, fila_2], columns = columnas)
df_2 = pd.DataFrame({"Nombre": nombres, "Apellido": apellidos, "Edad": edades})
df_3 = pd.DataFrame(list(zip(nombres, apellidos, edades)), columns = columnas)

# Mostrar los DataFrames
print("DataFrame a partir de filas:\n", df_1)
print("\nDataFrame a partir de diccionario:\n", df_2)
print("\nDataFrame a partir de zip:\n", df_3)