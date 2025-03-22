# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

start_time = time.time()

# Step 1: Generate Sample Data (for visualization)
np.random.seed(42)  # Ensure reproducibility
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Step 2: Apply K-Means Clustering
k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
y_kmeans = kmeans.fit_predict(X)  # Assign each point to a cluster

# Step 3: Plot the Clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', alpha=0.6, edgecolors='k', label="Data Points")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            s=200, c='red', marker='X', label="Centroids")  # Plot cluster centers
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.legend()
plt.show()


end_time = time.time()
execution_time = end_time - start_time

print(f"Execution Time : {execution_time :.4f}")