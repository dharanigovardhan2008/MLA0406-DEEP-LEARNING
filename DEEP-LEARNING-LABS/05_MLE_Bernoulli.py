import numpy as np

# Bernoulli Dataset
data = np.array([1, 0, 1, 1, 0, 1, 1, 1, 0, 1])

# Number of Successes
success = np.sum(data)

# Total Observations
n = len(data)

# MLE Estimate
p = success / n

print("Dataset:")
print(data)

print("\nNumber of Successes:", success)

print("Total Observations:", n)

print("Estimated Probability (p):", p)

print("Estimated Probability (1-p):", 1 - p)
