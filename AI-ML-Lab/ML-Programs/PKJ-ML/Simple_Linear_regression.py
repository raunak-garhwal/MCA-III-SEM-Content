# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import time  # Import time module to measure execution time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Start time measurement
start_time = time.time()

# Step 1: Generate Sample Data (Random Data for Example)
np.random.seed(42)  # Ensure reproducibility
X = 2 * np.random.rand(100, 1)  # Independent variable
y = 4 + 3 * X + np.random.randn(100, 1)  # Dependent variable (with some noise)

# Step 2: Split the data into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create and Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make Predictions
y_pred = model.predict(X_test)

# Step 5: Print Model Parameters
print(f"Intercept (b): {model.intercept_[0]}")
print(f"Slope (m): {model.coef_[0][0]}")

# Step 6: Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")

# Step 7: Visualize the Results
plt.scatter(X_test, y_test, color='blue', label="Actual Data")  # Actual data points
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Regression Line")  # Predicted line
plt.xlabel("Independent Variable (X)")
plt.ylabel("Dependent Variable (y)")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()

# End time measurement
end_time = time.time()
execution_time = end_time - start_time  # Calculate execution time

# Print execution time
print(f"Execution Time: {execution_time:.4f} seconds")
