import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the data
data = pd.read_csv('datamultiple.csv')

# Check for missing values
if data.isnull().sum().any():
    print("Missing values found in the dataset. Please handle them before proceeding.")
    print(data.isnull().sum())
else:
    print("No missing values found.")

# Check data types
print("Data types:\n", data.dtypes)

# Step 2: Define features and target variable
X = data[['feature1', 'feature2', 'feature3']]  # Features
y = data['target']  # Target variable

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create a linear regression model
model = LinearRegression()

# Step 5: Fit the model to the training data
model.fit(X_train, y_train)

# Step 6: Make predictions on the test data
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Optional: Print the coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
