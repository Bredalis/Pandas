
import pandas as pd

# DF

df = pd.DataFrame({
	"Numeros": [1, 2, 3, 4], 
	"Letras": ["a", "b", "c", "d"]
})

print(f"DF: \n{df}")
print(f"Selecion de posicion de filas: \n{df.iloc[:3]}")
print("\nOrdenados de forma descendente:\n", 
	df.sort_values("Numeros", ascending = False))

# Devuelve los numeros de esa columna en negativo

print(df["Numeros"].apply(lambda x: -x))