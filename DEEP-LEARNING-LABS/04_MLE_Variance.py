import numpy as np

# Dataset
data = np.array([12, 15, 18, 20, 22, 25, 28])

# Calculate Mean
mean = np.mean(data)

# Calculate MLE Variance
variance = np.sum((data - mean) ** 2) / len(data)

print("Dataset:")
print(data)

print("\nMean:", mean)

print("MLE Variance:", variance)

print("\nStandard Deviation:", np.sqrt(variance))
