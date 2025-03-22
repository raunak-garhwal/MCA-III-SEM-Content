import random
import csv

# Step 1: Generate a random dataset and save it to a CSV file
num_samples = 100  # Number of rows
num_features = 3   # Number of features (X1, X2, X3)

# Create a list to store the rows
dataset = []

# Generate random values for the dataset
for _ in range(num_samples):
    # Generate random feature values
    features = [random.uniform(1, 10) for _ in range(num_features)]
    # Generate a random target value (dependent variable)
    target = 5 + sum(features) + random.uniform(-5, 5)  # Linear relation with noise
    dataset.append(features + [target])

# Save the dataset to a CSV file
header = ['X1', 'X2', 'X3', 'Y']
with open('random_dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(dataset)

print("Dataset saved to 'random_dataset.csv'")

# Step 2: Read data from the CSV file
data = []
with open('random_dataset.csv', 'r') as file:
    next(file)  # Skip the header row
    for line in file:
        data.append([float(x) for x in line.strip().split(',')[1:]])

# Step 3: Separate features (X) and target (Y)
X = [row[:-1] for row in data]  # All columns except the last one (features)
Y = [row[-1] for row in data]   # The last column (target)

# Step 4: Add a column of ones to X for the intercept (bias term)
X = [[1] + row for row in X]  # Adds a 1 to the start of each row in X for the intercept

# Step 5: Perform Multiple Linear Regression using the Normal Equation
# Beta = (X.T * X)^(-1) * X.T * Y
# First, we calculate X.T * X
XtX = [[sum(X[i][k] * X[j][k] for i in range(len(X))) for j in range(len(X[0]))] for k in range(len(X[0]))]

# Next, calculate the inverse of XtX (using Gaussian elimination or other methods)
def matrix_inverse(matrix):
    # We are going to implement the Gauss-Jordan elimination to find the inverse
    n = len(matrix)
    augmented_matrix = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]
    
    # Perform Gauss-Jordan elimination
    for i in range(n):
        # Make the diagonal element 1
        diag = augmented_matrix[i][i]
        for j in range(2 * n):
            augmented_matrix[i][j] /= diag

        # Make all other elements in column i 0
        for j in range(n):
            if i != j:
                ratio = augmented_matrix[j][i]
                for k in range(2 * n):
                    augmented_matrix[j][k] -= ratio * augmented_matrix[i][k]

    # The inverse is on the right side of the augmented matrix
    return [row[n:] for row in augmented_matrix]

XtX_inv = matrix_inverse(XtX)

# Now calculate X.T * Y
XtY = [sum(X[i][j] * Y[i] for i in range(len(X))) for j in range(len(X[0]))]

# Calculate the coefficients (beta)
beta = [sum(XtX_inv[i][j] * XtY[j] for j in range(len(XtX_inv[0]))) for i in range(len(XtX_inv))]

# Print the coefficients (beta values)
print("\nCoefficients (including intercept):")
print(beta)

# Step 6: Make predictions
Y_pred = [sum(beta[j] * X[i][j] for j in range(len(beta))) for i in range(len(X))]

# Step 7: Calculate the Mean Squared Error (MSE)
mse = sum((Y[i] - Y_pred[i]) ** 2 for i in range(len(Y))) / len(Y)
print(f"\nMean Squared Error: {mse}")

# Optional: Print predicted vs actual values
print("\nPredictions vs Actual (first 10 samples):")
for i in range(10):
    print(f"Predicted: {Y_pred[i]:.2f}, Actual: {Y[i]:.2f}")
