
import pandas as pd

# DF

datos = pd.read_csv("../CSV/Clientes.csv")

print("Buscar datos faltantes: \n", datos["nombre"].isnull())
print("\nBorrar datos faltantes: \n", datos.dropna())

datos.dropna(subset = ["nombre", "ingreso"], inplace = True)
print(datos)

# Valores para sustitur los datos en NaN

valores_para_sustituir = {
	"nombre": "Desconocido",
	"edad": 18,
	"ingreso": 10000
}

print("\nDF con los datos NaN sustituidos: \n", 
	datos.fillna(value = valores_para_sustituir))

# Mostrar datos

print("\nPromedio:", datos["ingreso"].mean())
print("Media:", datos["ingreso"].median())
print("Moda:", datos["ingreso"].mode())