
# Librerias

import pandas as pd
import numpy as np

# DF

df = pd.DataFrame({	
	"Frutas": ["Sandia", "Aguacate", "Manzana", "Guineo"],
	"Calificacion": [10, 2, 7, 9]
})

print(f"DF: \n{df}")

# Manipulando valores

df["Calificacion"][:2] = np.nan

print(f"\nSustitucion de valores: \n{df["Calificacion"].fillna(1)}")
print(f"\nDF: \n{df.head()}")