
import pandas as pd

# Define columns and rows
columns = ["First_Name", "Last_Name", "Age"]
row_1 = ["Juliana", "Perez", 17]
row_2 = ["Perla", "Ramirez", 28]

# Lists of data
first_names = ["Julia", "Pedro", "Joaquin"]
last_names = ["De La Cruz", "Ramos", "Mercedes"]
ages = [44, 25, 39]

# Create DataFrames
df_from_rows = pd.DataFrame([row_1, row_2], columns=columns)
df_from_dict = pd.DataFrame({
    "First_Name": first_names,
    "Last_Name": last_names,
    "Age": ages
})
df_from_zip = pd.DataFrame(list(zip(first_names, last_names, ages)), columns=columns)

# Display the DataFrames
print("DataFrame from rows:\n", df_from_rows)
print("\nDataFrame from dictionary:\n", df_from_dict)
print("\nDataFrame from zip:\n", df_from_zip)
