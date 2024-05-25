
# Librerias

import pandas as pd
import matplotlib.pyplot as plt

# DF

df = pd.DataFrame({
	"Coordenadas": [1, 6, 3, 8]
})

# Grafica

df.plot()

plt.title("Grafica")
plt.show()