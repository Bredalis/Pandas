
import pandas as pd

# Dictionary of data to create DataFrame
data_1 = {
    "Name": ["Perla", "Pedro", "Pedrito"],
    "Age": [23, 24, 25],
    "Country": ["Puerto Rico", "RD", "Chile"],
}

# Create DataFrames
df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame({
    "Colors": ["Red", "Green", "Blue", "Orange"],
    "Score": [5, 7, 9, 0],
})

# Display information and content of DataFrames
print(f"Size of df_1: {df_1.shape}")
print(f"\nHeader of df_1:\n{df_1.head()}")
print(f"\nDescription of df_1:\n{df_1.describe()}")
print(f"\nContent of df_1:\n{df_1}")
print(f"\nContent of df_2:\n{df_2}")

# Update column names in df_2
df_2.columns = ["Colors", "Score"]
print(f"\nUpdated content of df_2:\n{df_2}")
