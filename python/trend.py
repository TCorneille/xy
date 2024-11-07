import matplotlib.pyplot as plt

# Sample monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [1200, 1350, 1500, 1700, 1600, 1800, 2000, 2100, 2300, 1000, 2500, 2700]

# Plotting the trend line
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', color='green', linestyle='-', linewidth=2)

# Adding labels and title
plt.title("Monthly Sales Trend Over One Year")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)

# Display the trend plot
plt.show()
