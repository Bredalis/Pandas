
import pandas as pd

# DataFrames
derecha = pd.DataFrame({
	"Key": range(5),
	"Right_Value": [1, 2, 3, 4, 5]
})

izquierda = pd.DataFrame({
	"Key": range(2, 7),
	"Left_Value": [1, 2, 3, 4, 5]
})

# Mostrar resultados de concatenación y unión
print(f"Concatenación Vertical (filas):\n{pd.concat([derecha, izquierda])}")
print("\nConcatenación Horizontal (columnas):\n",
	pd.concat([derecha, izquierda], axis = 1))

print(f"\nUnión (merge):\n{pd.merge(derecha, izquierda, on = "Key")}")