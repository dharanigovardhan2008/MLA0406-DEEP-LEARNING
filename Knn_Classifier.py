import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [2, 3],
    [3, 4],
    [4, 5],
    [6, 7],
    [7, 8],
    [8, 9]
])

y = np.array([0, 0, 0, 1, 1, 1])

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X, y)

# Test sample
test = np.array([[5, 6]])

# Predict class
prediction = model.predict(test)

print("Training Data:")
print(X)

print("\nTarget Classes:")
print(y)

print("\nTest Data:", test)

print("Predicted Class:", prediction[0])
