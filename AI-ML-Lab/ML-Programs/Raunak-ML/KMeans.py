import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ✅ Step 1: Load Data from CSV
df = pd.read_csv("ML-Programs/Raunak-ML/KMeans_Dataset.csv")

# ✅ Step 2: Select Features for Clustering
X = df[['Annual_Income', 'Spending_Score']].values  # Taking relevant features

# ✅ Step 3: Standardize the Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Normalize data for better clustering

# ✅ Step 4: Find Optimal Number of Clusters using Elbow Method
wcss = []  # Within-cluster sum of squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)  # Store WCSS for each K

# Plot Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--', color='b')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS (Within Cluster Sum of Squares)")
plt.title("Elbow Method for Optimal K")
plt.grid()
plt.show()

# ✅ Step 5: Train K-Means Model with Optimal Clusters (Assume K=3)
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)  # Assign cluster labels

# ✅ Step 6: Visualization of Clusters
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=df['Cluster'], cmap='viridis', edgecolor='k', s=100, alpha=0.75)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=250, c='red', marker='X', label='Centroids')
plt.xlabel("Annual Income (Normalized)")
plt.ylabel("Spending Score (Normalized)")
plt.title("K-Means Clustering on Customer Data")
plt.legend()
plt.grid()
plt.show()
