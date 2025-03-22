import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import for 3D visualization
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ✅ Load Dataset from CSV File
df = pd.read_csv("ML-Programs\Raunak-ML\MLR.csv")  # Ensure file path is correct

# ✅ Splitting Dataset into Independent (X) and Dependent (Y) Variables
X = df[['X1', 'X2', 'X3']]  # Independent Variables (Features)
Y = df['Y']  # Dependent Variable (Target)

# ✅ Train the Multiple Linear Regression Model
model = LinearRegression()
model.fit(X, Y)  # Fit the model with X and Y

# ✅ Get Model Coefficients & Intercept
coefficients = model.coef_  # Slopes for each independent variable (X1, X2, X3)
intercept = model.intercept_  # Intercept value

# Print Model Information
print("\n✅ Model Trained Successfully!\n")
print(f"Model Coefficients (Slopes): {coefficients}")  # Coefficients for each feature
print(f"Model Intercept: {intercept}")  # Intercept value

# ✅ Predict Y values using the trained model
Y_pred = model.predict(X)  # Predicted Y values based on input X

# ✅ Calculate Mean Squared Error (MSE) - Measures model accuracy
mse = mean_squared_error(Y, Y_pred)
print(f"Mean Squared Error (MSE): {mse}")

# ✅ Scatter Plots: Each Feature vs Target (Y)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # Create subplots for 3 features

# Loop through each feature and plot scatter plots
for i, feature in enumerate(['X1', 'X2', 'X3']):
    axes[i].scatter(df[feature], Y, color='blue', label=f'Actual {feature} vs Y')  # Scatter plot
    axes[i].set_xlabel(feature)  # X-axis label
    axes[i].set_ylabel('Y')  # Y-axis label
    axes[i].set_title(f'{feature} vs Y')  # Title for each subplot
    axes[i].legend()  # Show legend

plt.show()  # Display all scatter plots

# ✅ 3D Scatter Plot (X1, X2 vs Y) for Visualization
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')  # Add 3D subplot

ax.scatter(df['X1'], df['X2'], Y, color='blue', label='Actual Data')  # Scatter plot in 3D
ax.set_xlabel("X1 - Feature 1")  # Label X-axis
ax.set_ylabel("X2 - Feature 2")  # Label Y-axis
ax.set_zlabel("Y - Target")  # Label Z-axis
ax.set_title("3D Scatter Plot: X1 & X2 vs Y")  # Plot title

plt.show()  # Show 3D scatter plot
