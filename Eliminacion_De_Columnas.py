
import pandas as pd

# Crear y mostar df

df = pd.read_csv("All_bikez_curated.csv") 
print(f"DF: \n{df.head()}")

print(df.dtypes)

# Eliminacion de este tipo de dato

df = df.select_dtypes(exclude = ["object"])
print("\nDF sin object: \n", df)