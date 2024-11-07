import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load a dataset
df = sns.load_dataset('tips')

# Set the theme and style
sns.set_style('whitegrid')

# Create a scatter plot with a regression line
sns.lmplot(x='total_bill', y='tip', data=df, hue='sex', markers=['o', 'x'])

# Customize the plot with titles and labels
plt.title('Total Bill vs Tip with Gender')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')

# Show the plot
plt.show()
