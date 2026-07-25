import numpy as np
from sklearn.neural_network import BernoulliRBM

# Sample Dataset
# 1 = Likes, 0 = Doesn't Like
# Movies watched by different users
X = np.array([
    [1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1]
])

# Create RBM Model
rbm = BernoulliRBM(
    n_components=2,
    learning_rate=0.1,
    n_iter=100,
    random_state=42
)

# Train the RBM
rbm.fit(X)

# Transform the data into hidden features
hidden_features = rbm.transform(X)

print("Original Data:")
print(X)

print("\nHidden Features Learned by RBM:")
print(np.round(hidden_features, 3))
