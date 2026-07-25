import numpy as np
from sklearn.neural_network import MLPClassifier

# Training Dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# XOR Output
y = np.array([0, 1, 1, 0])

# Create Neural Network
model = MLPClassifier(hidden_layer_sizes=(4,),
                      max_iter=5000,
                      random_state=1)

# Train the model
model.fit(X, y)

# Predict Output
prediction = model.predict(X)

print("Training Data:")
print(X)

print("\nActual Output:")
print(y)

print("\nPredicted Output:")
print(prediction)

print("\nTraining Accuracy:", model.score(X, y))
