import pandas as pd

# Load the dataset
data = pd.read_csv("/Users/divyanshu/Downloads/dataset_500.csv")  # Ensure the correct path to your CSV

# Debugging step: Print column names
print("Columns in dataset:", data.columns)

# Strip spaces and retry if needed
data.columns = data.columns.str.strip()

# Now try selecting features
X = data[['feature1', 'feature2', 'feature3']]
