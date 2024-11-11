
import pandas as pd

# Diccionario de datos para crear el DataFrame
datos = {
	"Nombres": ["Yulissa", "Juanmy", "Lucas"],
	"Edad": [37, 25, 27],
	"DNI": ["480140", "40856", "48976"]
}

# Creación de DataFrame
df = pd.DataFrame(datos)
print(f"DataFrame:\n{df}")

# Agregar columnas (de distintas formas) al DataFrame
df["Profesiones"] = ["Ingeniero", "Maestro", "Bombero"] # Sintaxis básica
df = df.assign(Sueldo = [200, 100, 400]) # Asignando
df.insert(3, "Numeros", [52, 67, 80]) # Insertando

# Mostrar DataFrame resultante
print(f"\nDataFrame actualizado:\n{df}")