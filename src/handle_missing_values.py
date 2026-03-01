
import numpy as np
import pandas as pd


# Create DataFrame
df = pd.DataFrame({
    "Fruits": ["Watermelon", "Avocado", "Apple", "Banana"],
    "Rating": [10, 2, 7, 9]
})

print(f"Original DataFrame:\n{df}")

# Assign NaN values to the first two values in the 'Rating' column
df.loc[:1, "Rating"] = np.nan

print(f"\nDataFrame with NaN values:\n{df}")

# Fill NaN values with 1 in 'Rating'
df["Rating"] = df["Rating"].fillna(1)

print(f"\nDataFrame with NaN values replaced:\n{df}")
