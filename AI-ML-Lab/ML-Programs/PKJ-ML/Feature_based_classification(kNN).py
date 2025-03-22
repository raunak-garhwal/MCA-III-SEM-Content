# Import required libraries
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Start time measurement
start_time = time.time()

# Step 1: Load the dataset (Iris dataset)
iris = datasets.load_iris()
X = iris.data  # Features: Sepal length, Sepal width, Petal length, Petal width
y = iris.target  # Target: Flower species (Setosa, Versicolor, Virginica)

# Step 2: Split dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Apply k-NN Algorithm (k=5)
k = 5  # Number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)  # Initialize the model
knn.fit(X_train, y_train)  # Train the model

# Step 4: Make Predictions
y_pred = knn.predict(X_test)

# Step 5: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Print detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Print Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 6: Visualizing Feature Importance (Sepal vs Petal)
plt.scatter(X[:, 0], X[:, 2], c=y, cmap="viridis", edgecolors='k')
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Feature-Based Classification (Sepal vs Petal)")
plt.colorbar(label="Flower Species")
plt.show()

# End time measurement
end_time = time.time()
execution_time = end_time - start_time  # Calculate execution time

# Print execution time
print(f"Execution Time: {execution_time:.4f} seconds")
