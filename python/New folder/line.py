import matplotlib.pyplot as plt


# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 6, 8, 10, 9, 12, 14]

# Create the line plot
plt.plot(x, y, color='green', marker='o', linestyle='dashdot', linewidth=2, markersize=6)

# Add titles and labels
plt.title('Sample Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Show the plot
plt.show()
