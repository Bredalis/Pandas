
import pandas as pd

# DF

df = pd.DataFrame({	
	"Nombres": ["Yulissa", "Juanmi", "Lucas"],
	"Edad": [37, 25, 27],
	"DNI": ["480140", "40856", "48976"]
})

# Maneras de seleccionar filas de un DF

print("Metodo para revisar si hay un determinado dato: \n",
	df.Nombres.isin(["Yulissa", "Perla"]))

print("\nSintaxis basica: \n", df[df["Nombres"] == "Lucas"])
print("\n", df.iloc[[0, 1], [0, 2]])

# Poner la columna Nombres como index

nombres = df.set_index("Nombres")

# Mostrar datos

print(f"\nNombres como index: \n{nombres}")
print(f"\nDF: \n{df}")