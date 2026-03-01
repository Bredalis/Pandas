
import pandas as pd
import matplotlib.pyplot as plt


# Create DataFrame
df = pd.DataFrame({"Coordinates": [1, 6, 3, 8]})

# Plot data
df.plot(title="Chart")
plt.show()
