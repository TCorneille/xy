import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data for the heatmap
data = np.random.rand(10, 12)  # 10 rows and 12 columns

# Create a heatmap using seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(data, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)

# Add title and labels
plt.title('Heatmap Example')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')

# Show the plot
plt.show()
