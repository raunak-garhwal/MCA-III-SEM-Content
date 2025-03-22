# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Start time measurement
start_time = time.time()

# Step 1: Generate a small synthetic dataset with valid feature counts
X, y = make_classification(
    n_samples=50, n_features=2, 
    n_informative=2, n_redundant=0, n_repeated=0, 
    n_classes=2, n_clusters_per_class=1, random_state=42
)

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Apply k-NN Algorithm
k = 3  # Number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)  # Initialize the model
knn.fit(X_train, y_train)  # Train the model

# Step 4: Make predictions
y_pred = knn.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Step 6: Visualize the decision boundary
xx, yy = np.meshgrid(np.linspace(X[:, 0].min()-1, X[:, 0].max()+1, 100),
                     np.linspace(X[:, 1].min()-1, X[:, 1].max()+1, 100))

Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, edgecolors='k', cmap='coolwarm', label="Test Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title(f"k-NN Classification (k={k})")
plt.legend()
plt.show()

# End time measurement
end_time = time.time()
execution_time = end_time - start_time  # Calculate execution time

# Print execution time
print(f"Execution Time: {execution_time:.4f} seconds")
