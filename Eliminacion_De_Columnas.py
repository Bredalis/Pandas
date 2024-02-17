
import pandas as pd

ruta = 'C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Datasets/CSV/Cars/all_bikez_curated.csv'

# Crear y mostar df

df = pd.read_csv(ruta) 
print(f'DF: \n{df.head()}')

print(df.dtypes)

# Eliminacion

df = df.select_dtypes(exclude = ['object'])
print('\nDF sin object: \n', df)