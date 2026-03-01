
import pandas as pd

# DataFrames
right_df = pd.DataFrame({
    "Key": range(5),
    "Right_Value": [1, 2, 3, 4, 5],
})

left_df = pd.DataFrame({
    "Key": range(2, 7),
    "Left_Value": [1, 2, 3, 4, 5],
})

# Vertical concatenation (stacking rows)
vertical_concat = pd.concat([right_df, left_df])
print(f"Vertical Concatenation (rows):\n{vertical_concat}")

# Horizontal concatenation (stacking columns)
horizontal_concat = pd.concat([right_df, left_df], axis=1)
print("\nHorizontal Concatenation (columns):\n", horizontal_concat)

# Merge DataFrames on the 'Key' column
merged_df = pd.merge(right_df, left_df, on="Key")
print(f"\nMerge on 'Key':\n{merged_df}")
