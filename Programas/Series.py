
import pandas as pd

# Creación de una Serie
serie = pd.Series(
	["Masa", "Peso", "Volumen"], 
	name = "Componentes de la Materia"
)

# Mostrar la Serie
print(f"Serie:\n{serie}")