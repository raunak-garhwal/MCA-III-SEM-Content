import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
data = pd.read_csv('ML-Programs\Raunak-ML\logisticclassification-data.csv')  # Ensure the file name is correct

# Check the distribution of classes
print(data['label'].value_counts())

# Step 2: Prepare the features and labels
X = data[['feature1', 'feature2']]  # Replace with your feature columns
y = data['label']  # Replace with your label column

# Step 3: Split the dataset into training and testing sets
# Remove stratify if you have a very small dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Removed stratify=y

# Step 4: Create the logistic regression model
model = LogisticRegression()

# Step 5: Fit the model
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy * 100:.2f}%')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(class_report)

# Optional: Predicting a new sample
new_sample = pd.DataFrame([[5.0, 3.5]], columns=['feature1', 'feature2'])  # Replace with your new sample values
prediction = model.predict(new_sample)
print(f'Predicted class for {new_sample.values[0]}: {prediction[0]}')
