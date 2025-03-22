import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
# Replace 'population_data.csv' with the path to your CSV file
data = pd.read_csv('ML-Programs\Raunak-ML\Population_data.csv')

# Check the first few rows of the dataframe
print(data.head())

# Extract the country names and population values
labels = data['Country']
sizes = data['Population']

# Define colors for each slice
colors = plt.cm.tab20.colors  # You can choose a different colormap if you want

# Create a pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

# Title of the pie chart
plt.title('Population Distribution by Country')

# Show the pie chart
plt.show()
