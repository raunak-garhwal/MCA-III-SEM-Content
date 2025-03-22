# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time  # Import time module to measure execution time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Start time measurement
start_time = time.time()

# Step 1: Create a Small Dataset
data = {
    'Study_Hours': [2, 3, 5, 7, 9, 11, 13, 15],  # Independent Variable 1
    'Sleep_Hours': [8, 7, 7, 6, 6, 5, 5, 4],     # Independent Variable 2
    'Exercise_Hours': [1, 2, 2, 3, 3, 4, 4, 5],  # Independent Variable 3
    'Exam_Score': [50, 55, 65, 70, 75, 80, 85, 90]  # Dependent Variable (Y)
}

df = pd.DataFrame(data)  # Convert to DataFrame
print(df)  # Print the dataset

# Step 2: Split Features (X) and Target Variable (y)
X = df[['Study_Hours', 'Sleep_Hours', 'Exercise_Hours']]  # Independent Variables
y = df['Exam_Score']  # Dependent Variable

# Step 3: Split Data into Training and Testing Sets (75% Train, 25% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 4: Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make Predictions
y_pred = model.predict(X_test)

# Step 6: Print Model Parameters
print(f"Intercept (b): {model.intercept_}")
print(f"Coefficients (m1, m2, m3): {model.coef_}")

# Step 7: Compare Predictions with Actual Values
results = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print(results)

# Step 8: Visualization
plt.scatter(y_test, y_pred, color='blue', alpha=0.7, label="Predicted vs Actual")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='dashed', label="Perfect Fit")
plt.xlabel("Actual Exam Score")
plt.ylabel("Predicted Exam Score")
plt.title("Multiple Linear Regression: Predictions vs Actual")
plt.legend()
plt.show()


# End time measurement
end_time = time.time()
execution_time = end_time - start_time  # Calculate execution time

# Print execution time
print(f"Execution Time: {execution_time:.4f} seconds")
