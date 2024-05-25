
import pandas as pd

# Creacion de una Serie

serie = pd.Series(["Masa", "Peso", "Volumen"])
serie.name = "Componentes de la Materia"

print("Serie: \n", serie)