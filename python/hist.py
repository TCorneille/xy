import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9]

# Define custom bins to combine values 4 and 5
bins = range(1, 11) # The bin from 4 to 6 includes both 4 and 5

# Create histogram
plt.hist(data, bins=bins, color='skyblue', edgecolor='black')

# Labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Sample Histogram (Combined 4 and 5)')

# Display the plot
plt.show()
