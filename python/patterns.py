import matplotlib.pyplot as plt

# Sample data: average monthly temperatures over two years (in degrees Celsius)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
year_1_temps = [5, 7, 12, 16, 20, 24, 28, 27, 22, 17, 11, 6]
year_2_temps = [6, 8, 13, 17, 21, 25, 29, 28, 23, 18, 12, 7]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(months, year_1_temps, marker='o', label="Year 1", color='blue')
plt.plot(months, year_2_temps, marker='o', label="Year 2", color='green')

# Adding labels and title
plt.title("Monthly Temperature Patterns Over Two Years")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
