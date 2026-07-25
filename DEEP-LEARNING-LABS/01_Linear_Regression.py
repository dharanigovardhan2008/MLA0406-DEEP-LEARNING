import numpy as np
from sklearn.linear_model import LinearRegression

# Training dataset
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([10, 20, 30, 40, 50, 60])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Test dataset
X_test = np.array([[7], [8]])

# Predict output
y_pred = model.predict(X_test)

print("Training Data (X):")
print(X)

print("\nActual Output (Y):")
print(y)

print("\nPredicted Output:")
print(y_pred)

print("\nSlope:", model.coef_[0])
print("Intercept:", model.intercept_)
