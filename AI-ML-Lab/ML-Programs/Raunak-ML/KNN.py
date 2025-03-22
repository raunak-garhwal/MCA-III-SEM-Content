import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ✅ Step 1: Load Data from CSV
df = pd.read_csv("ML-Programs/Raunak-ML/KNN_Dataset.csv")

# ✅ Step 2: Select Features (X) and Target Variable (Y)
X = df[['Age', 'Annual_Income', 'Spending_Score']].values  # Independent Variables
Y = df['Label'].values  # Target Variable

# ✅ Step 3: Split Data into Train and Test Sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# ✅ Step 4: Standardize the Data (Improves KNN Performance)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ✅ Step 5: Train KNN Model (Choosing K=5)
knn_model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn_model.fit(X_train, Y_train)

# ✅ Step 6: Predict Using the Model
Y_pred = knn_model.predict(X_test)

# ✅ Step 7: Evaluate Model Performance
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Print Classification Report & Confusion Matrix
print("\nClassification Report:")
print(classification_report(Y_test, Y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(Y_test, Y_pred))

# ✅ Step 8: Visualizing the Decision Boundary (Only for 2D Projection)
plt.figure(figsize=(8, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=Y_test, cmap='coolwarm', edgecolor='k', label="Actual Data")

# Plot Predicted Points with Different Marker
plt.scatter(X_test[:, 0], X_test[:, 1], c=Y_pred, cmap='coolwarm', marker='x', alpha=0.7, label="Predicted Data")

plt.xlabel('Age (Standardized)')
plt.ylabel('Annual Income (Standardized)')
plt.title('KNN Classification')
plt.legend()
plt.grid()
plt.show()
