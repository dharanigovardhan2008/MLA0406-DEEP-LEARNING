import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Dataset (Age, Salary)
X = np.array([
    [22, 25000],
    [25, 30000],
    [30, 40000],
    [35, 60000],
    [40, 70000],
    [45, 80000]
])

# Target (0 = No Purchase, 1 = Purchase)
y = np.array([0, 0, 0, 1, 1, 1])

# Create Decision Tree model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Test data
test = np.array([[38, 65000]])

# Prediction
prediction = model.predict(test)

print("Training Data:")
print(X)

print("\nTarget Values:")
print(y)

print("\nTest Data:", test)

print("Predicted Class:", prediction[0])
