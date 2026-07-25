import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# Actual and Predicted Classes
actual = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 1])
predicted = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 1])

# Generate Confusion Matrix
cm = confusion_matrix(actual, predicted)

# Calculate Accuracy
accuracy = accuracy_score(actual, predicted)

print("Actual Classes:")
print(actual)

print("\nPredicted Classes:")
print(predicted)

print("\nConfusion Matrix:")
print(cm)

print("\nAccuracy:", accuracy)
