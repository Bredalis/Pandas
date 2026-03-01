
import pandas as pd

# Create the DataFrame
df = pd.DataFrame({
    "Numbers": [1, 2, 3, 4],
    "Letters": ["a", "b", "c", "d"]
})

# Display DataFrame information
print(f"Complete DataFrame:\n{df}")
print(f"\nFirst three rows:\n{df.iloc[:3]}")

# DataFrame sorted by 'Numbers' in descending order
print("\nDataFrame sorted by 'Numbers' descending:\n",
      df.sort_values("Numbers", ascending=False))

# Convert numbers to negative values in the 'Numbers' column
print("\nNegative values in 'Numbers' column:\n",
      df["Numbers"].apply(lambda x: -x))
