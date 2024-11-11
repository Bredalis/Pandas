
import pandas as pd
import numpy as np

# Crear el DataFrame
df = pd.DataFrame({	
	"Frutas": ["Sandía", "Aguacate", "Manzana", "Guineo"],
	"Calificacion": [10, 2, 7, 9]
})

print(f"DataFrame original:\n{df}")

# Asignar los valores NaN a los primeros dos valores en la columna 'Calificacion'
df.loc[:1, "Calificacion"] = np.nan

print(f"\nDataFrame con valores NaN:\n{df}")

# Rellenar los valores NaN con 1 en 'Calificacion'
df["Calificacion"] = df["Calificacion"].fillna(1) 

print(f"\nDataFrame con los valores NaN sustituidos:\n{df}")