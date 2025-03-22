import numpy as np
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [30, 40, 20, 50, 35]  # Values for the bar graph
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Create a bar graph
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=colors, alpha=0.7, edgecolor='black')

# Add title and labels
plt.title("Bar Graph Example", fontsize=14)
plt.xlabel("Categories", fontsize=12)
plt.ylabel("Values", fontsize=12)

# Add grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the bar graph
plt.show()

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})

# Add title
plt.title("Pie Chart Example", fontsize=14)

# Show the pie chart
plt.show()