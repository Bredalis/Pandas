
import pandas as pd


# Create DataFrame
df = pd.DataFrame({
    "Names": ["Yulissa", "Juanmy", "Lucas"],
    "Age": [37, 25, 27],
    "ID": ["480140", "40856", "48976"]
})

# Ways to select rows from DataFrame
print("Method to check for specific data:\n", df.Names.isin(["Yulissa", "Perla"]))
print("\nBasic selection:\n", df[df["Names"] == "Lucas"])
print("\nSelect by position:\n", df.iloc[[0, 1], [0, 2]])

# Set 'Names' column as index
indexed_names = df.set_index("Names")

# Display data
print("\nDataFrame with 'Names' as index:\n", indexed_names)
print("\nOriginal DataFrame:\n", df)
