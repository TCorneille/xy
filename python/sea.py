import seaborn as sns
import matplotlib.pyplot as plt
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
sns.distplot(data, kde=True)
plt.title('Distribution Plot')
plt.show()
