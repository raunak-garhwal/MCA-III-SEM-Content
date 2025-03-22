# Import necessary libraries
import pandas as pd  # For data handling
import matplotlib.pyplot as plt  # For visualization
from sklearn.linear_model import LinearRegression  # For Linear Regression Model
from sklearn.metrics import mean_squared_error  # For calculating error

# Load Dataset from CSV file
df = pd.read_csv('ML-Programs/Raunak-ML/SLR.csv')  # Ensure the correct path to your dataset

# Print column names to verify dataset structure
print("\nColumns in dataset:", df.columns)

# Strip spaces from column names (if any) to avoid errors
df.columns = df.columns.str.strip()

# Verify that required columns ('X' and 'Y') exist in the dataset
if 'X' not in df.columns or 'Y' not in df.columns:
    raise KeyError("Error: Column names 'X' and 'Y' not found in CSV. Check column names using print(df.columns).")

# Splitting the dataset into independent (X) and dependent (Y) variables
X = df[['X']]  # Independent Variable (Feature)
Y = df['Y']    # Dependent Variable (Target)

# Initializing the Linear Regression Model
model = LinearRegression()

# Training (Fitting) the model using given data
model.fit(X, Y)

# Extracting Model Coefficients
m = model.coef_[0]  # Slope of the regression line
c = model.intercept_  # Intercept (where the line crosses Y-axis)

# Printing Model Parameters
print(f"\n✅ Model Trained Successfully!\n")
print(f"Model Coefficient (Slope, m): {m}")
print(f"Model Intercept (c): {c}")

# Predicting Y values using the trained model
Y_pred = model.predict(X)

# Calculating Mean Squared Error (MSE) to evaluate model accuracy
mse = mean_squared_error(Y, Y_pred)
print(f"Mean Squared Error (MSE): {mse}")

# Plotting the Data Points (Actual) and Regression Line (Predicted)
plt.scatter(X, Y, color='blue', label='Actual Data')  # Scatter plot for actual data points
plt.plot(X, Y_pred, color='red', linestyle='--', label='Regression Line')  # Regression line

# Labeling the axes and title
plt.xlabel('X - Independent Variable')
plt.ylabel('Y - Dependent Variable')
plt.title('Simple Linear Regression')

# Adding a legend to distinguish between actual data and predicted regression line
plt.legend()

# Display the plot
plt.show()
