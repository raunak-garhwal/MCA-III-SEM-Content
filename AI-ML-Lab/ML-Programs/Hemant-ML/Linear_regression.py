import csv
import random

# Generate synthetic data and save to CSV
random.seed(42)
data = [(random.uniform(0, 2), 4 + 3 * x + random.gauss(0, 1)) for x in [random.uniform(0, 2) for _ in range(100)]]

with open("ML-Programs\Raunak-ML\Linear_regression-dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["X", "y"])
    writer.writerows(data)

# Load data from CSV
X, y = [], []
with open("ML-Programs\Raunak-ML\Linear_regression-dataset.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        X.append(float(row[0]))
        y.append(float(row[1]))

# Split data into training and testing sets
train_size = int(0.8 * len(X))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Implement simple linear regression
def mean(values):
    return sum(values) / len(values)

def covariance(x, mean_x, y, mean_y):
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))

def variance(values, mean_value):
    return sum((x - mean_value) ** 2 for x in values)

def coefficients(x, y):
    mean_x, mean_y = mean(x), mean(y)
    b1 = covariance(x, mean_x, y, mean_y) / variance(x, mean_x)
    b0 = mean_y - b1 * mean_x
    return b0, b1

def predict(x, b0, b1):
    return [b0 + b1 * xi for xi in x]

# Train the model
b0, b1 = coefficients(X_train, y_train)

# Make predictions
y_pred = predict(X_test, b0, b1)

# Evaluate the model
mse = sum((y_test[i] - y_pred[i]) ** 2 for i in range(len(y_test))) / len(y_test)

# Display results
print(f"Mean Squared Error: {mse}")
print(f"Model Coefficients: {b1}")
print(f"Model Intercept: {b0}")
