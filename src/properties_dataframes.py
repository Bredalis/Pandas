
import pandas as pd

# Dictionary to create the DataFrame
data = {
    "Country": ["RD", "Peru", "Brazil", "Colombia", "Venezuela"],
    "Capital": ["Santo Domingo", "Lima", "Brasilia", "Bogotá", "Caracas"],
    "Population": [10000, 10000, 10000, 1000, 1000]
}

# Creating DataFrames
df_full = pd.DataFrame(data)
df_partial = pd.DataFrame(data, columns=["Country", "Population"])
df_indexed = pd.DataFrame(
    data, index=data["Country"], columns=["Capital", "Population"]
)

# Display DataFrames
print("Full DataFrame:\n", df_full)
print("\nDataFrame head:\n", df_full.head())
print("\nDataFrame tail:\n", df_full.tail())
print("\nDataFrame rows 0 to 3:\n", df_full[0:4])

print("\nPartial DataFrame (Country and Population):\n", df_partial)

print("\nIndexed DataFrame (by Country):\n", df_indexed)
print("\nPopulation column in Indexed DataFrame:\n", df_indexed["Population"])

print(
    "\nPopulation of RD and Peru using loc:\n",
    df_indexed.loc[["RD", "Peru"], ["Population"]],
)
print(
    "\nPopulation of RD and Peru using iloc:\n",
    df_indexed.iloc[[0, 1], [1]],
)
