
import pandas as pd

# Dictionary of data to create the DataFrame
data = {
    "Names": ["Yulissa", "Juanmy", "Lucas"],
    "Age": [37, 25, 27],
    "ID": ["480140", "40856", "48976"],
}

# Create the DataFrame
df = pd.DataFrame(data)
print(f"Original DataFrame:\n{df}")

# Add columns to the DataFrame in different ways
df["Professions"] = ["Engineer", "Teacher", "Firefighter"]  # Basic syntax
df = df.assign(Salary=[200, 100, 400])  # Using assign method
df.insert(3, "Numbers", [52, 67, 80])  # Insert at specific position

# Show the updated DataFrame
print(f"\nUpdated DataFrame:\n{df}")
