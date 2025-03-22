import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset
data = pd.read_csv('/Users/divyanshu/Downloads/datak_500.csv')

# Step 2: Prepare the features and labels
X = data[['feature1', 'feature2']]  # Adjust column names if needed
y = data['label']

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create the k-NN classifier
k = 5  # You can choose any value for k
knn = KNeighborsClassifier(n_neighbors=k)

# Step 5: Fit the model
knn.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = knn.predict(X_test)

# Step 7: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'✅ Accuracy: {accuracy * 100:.2f}%\n')

# Print only the first 5 samples from the dataset
print("🔹 First 5 Rows of Data:\n", data.head(5))

# Optional: Predicting a new sample
new_sample = pd.DataFrame([[5.0, 3.5]], columns=['feature1', 'feature2'])
prediction = knn.predict(new_sample)
print(f'\n🔮 Predicted class for {new_sample.values[0]}: {prediction[0]}')
