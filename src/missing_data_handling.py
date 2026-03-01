
import pandas as pd

# Load the DataFrame
data = pd.read_csv("../csv/customers.csv")

# Check for missing values in the 'name' column
print("Missing values in 'name' column:\n", data["name"].isnull())

# Drop rows with any missing values
print("\nData without missing values:\n", data.dropna())

# Drop rows with NaN in specific columns: 'name' and 'income'
data.dropna(subset=["name", "income"], inplace=True)
print("\nData after dropping NaN in 'name' and 'income':\n", data)

# Values to replace NaN
replacement_values = {
    "name": "Unknown",
    "age": 18,
    "income": 10000
}

# Replace NaN in the DataFrame
print("\nDataFrame with NaN replaced:\n", data.fillna(value=replacement_values))

# Show statistics of the 'income' column
print("\nAverage income:", data["income"].mean())
print("Median income:", data["income"].median())
print("Mode of income:", data["income"].mode())
