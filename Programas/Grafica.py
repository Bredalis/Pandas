
import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame
df = pd.DataFrame({"Coordenadas": [1, 6, 3, 8]})

# Graficar los datos
df.plot(title = "Gráfica")
plt.show()