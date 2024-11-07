import matplotlib.pyplot as plt
import numpy as np

# Sample data
#data = [np.random.normal(loc=0, scale=1, size=100) for _ in range(5)]
Class_A_Scores = [78, 85, 89, 93, 70, 75, 60, 88, 92, 95] 
Class_B_Scores = [65, 78, 83, 85, 79, 90, 68, 80, 84, 88]
median_A = np.median(Class_A_Scores)
print("Median of Class B Scores:", median_A)
# Create the box plot
plt.boxplot([Class_A_Scores ,Class_B_Scores] , patch_artist=True)

# Add titles and labels
plt.title('Sample Box Plot')
plt.xlabel('classes')
plt.ylabel('scores')

# Customize the x-tick labels
plt.xticks([1, 2], ['Class A', 'Class B'])
#plt.xticks([1, 2, 3, 4, 5], ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'])

# Show the plot
plt.show()
