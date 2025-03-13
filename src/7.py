import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
data = pd.read_csv('data.csv')

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data[['feature1', 'feature2']], data['target'], test_size=0.3)

# Create a linear regression object
reg = LinearRegression()

# Train the model using the training data
reg.fit(X_train, y_train)

# Make predictions on the test data
y_pred = reg.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Use the trained model to make predictions on new data
new_data = pd.DataFrame({'feature1': [10], 'feature2': [20]})
prediction = reg.predict(new_data)[0]
print("Prediction:", prediction)