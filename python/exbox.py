import matplotlib.pyplot as plt

# Given data
Before_Studying = [65, 70, 68, 72, 69, 67, 71, 73, 68, 70]
After_Studying = [78, 82, 80, 85, 79, 81, 84, 86, 83, 80]

# Creating the box plots
plt.figure(figsize=(8, 6))
plt.boxplot([Before_Studying, After_Studying], labels=['Before Studying', 'After Studying'])

# Adding labels and title
plt.xlabel("Condition")
plt.ylabel("Test Scores")
plt.title("Effect of Studying on Test Scores")

# Display the plot
plt.show()
