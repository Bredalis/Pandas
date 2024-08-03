
"""
Diferentes formas de 
agregar columnas al df
"""

import pandas as pd

# Diccionario para df

datos = {
	"Nombres": ["Yulissa", "Juanmy", "Lucas"],
	"Edad": [37, 25, 27],
	"DNI": ["480140", "40856", "48976"]
}

# Creacion de df

df = pd.DataFrame(datos)
print(df)

df["Profesiones"] = ["Ingeniero", "Maestro", "Bombero"] # Sintaxis basica
df = df.assign(Sueldo = [200, 100, 400]) # Asignando
df.insert(3, "Numeros", [52, 67, 80]) # Insertando

# Mostrar df

print(f"\nDF: \n{df}")