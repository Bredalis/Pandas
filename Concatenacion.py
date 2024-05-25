
# Libreria

import pandas as pd

# DF

derecha = pd.DataFrame({
	"Key": range(5),
	"Right_Value": [1, 2, 3, 4, 5]
})

izquierda = pd.DataFrame({
	"Key": range(2, 7),
	"Left_Value": [1, 2, 3, 4, 5]
})

# Mostrar datos

print(f"Concatenacion Vertical (Filas): \n{pd.concat([derecha, izquierda])}")
print("\nConcatenacion Horizontal (Columnas): \n", 
	pd.concat([derecha, izquierda], axis = 1))

print(f"\nUnion: \n{pd.merge(derecha, izquierda, on = "Key")}")