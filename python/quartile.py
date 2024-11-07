import numpy as np

# Example dataset
data = [12, 15, 14, 10, 18, 20, 25, 30, 22, 28]

# Sort the data
sorted_data = np.sort(data)

# Calculate Q1 and Q3
Q1 = np.percentile(sorted_data, 25)
Q3 = np.percentile(sorted_data, 75)

print(f"Sorted Data: {sorted_data}")
print(f"First Quartile (Q1): {Q1}")
print(f"Third Quartile (Q3): {Q3}")
