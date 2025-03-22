import pandas as pd
from sklearn.cluster import KMeans

# Step 1: Load the data from the CSV file
data = pd.read_csv('/Users/divyanshu/Downloads/data.csv')

# Step 2: Prepare the data
X = data[['feature1', 'feature2']]  # Features for clustering

# Step 3: Apply K-means clustering
n_clusters = 3  # Specify the number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X)

# Step 4: Get the cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Step 5: Add the cluster labels to the original data
data['Cluster'] = labels

# Step 6: Print the results
print("Cluster Labels:")
print(data[['feature1', 'feature2', 'Cluster']])

print("\nCentroids of the clusters:")
print(centroids)
