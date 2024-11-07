import matplotlib.pyplot as plt

labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [25, 35, 20, 20]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart Example')
plt.show()
