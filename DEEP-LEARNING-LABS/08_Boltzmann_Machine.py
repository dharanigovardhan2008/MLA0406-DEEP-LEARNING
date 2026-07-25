import numpy as np
from sklearn.neural_network import BernoulliRBM

# Binary Dataset
X = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1]
])

# Create Bernoulli RBM
rbm = BernoulliRBM(n_components=2,
                   learning_rate=0.1,
                   n_iter=100,
                   random_state=0)

# Train Model
rbm.fit(X)

print("Training Dataset:")
print(X)

print("\nLearned Components:")
print(rbm.components_)

print("\nHidden Layer Output:")
print(rbm.transform(X))
