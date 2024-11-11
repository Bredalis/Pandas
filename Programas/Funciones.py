
import pandas as pd

# Crear el DataFrame
df = pd.DataFrame({
	"Numeros": [1, 2, 3, 4], 
	"Letras": ["a", "b", "c", "d"]
})

# Mostrar información del DataFrame
print(f"DataFrame completo:\n{df}")
print(f"\nPrimeras tres filas:\n{df.iloc[:3]}")
print("\nDataFrame ordenados por 'Numeros' en forma descendente:\n", 
	df.sort_values("Numeros", ascending = False))

# Convertir los números a negativos en la columna 'Numeros'
print("\nConvertir 'Numeros' con valores negativos:\n", 
	df["Numeros"].apply(lambda x: -x))