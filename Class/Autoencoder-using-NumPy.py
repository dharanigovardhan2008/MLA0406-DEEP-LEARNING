import numpy as np

# -----------------------------
# Student marks (Math, Science, English, Computer)
# -----------------------------
marks = np.array([[85, 90, 78, 88]])

print("Original Marks:")
print(marks)

# -----------------------------
# Encoder (4 -> 2)
# -----------------------------
encoder_weights = np.array([
    [0.5, 0.2],
    [0.4, 0.3],
    [0.3, 0.6],
    [0.2, 0.5]
])

# Encode the input
encoded = np.dot(marks, encoder_weights)

print("\nEncoded Features:")
print(encoded)

# -----------------------------
# Decoder (2 -> 4)
# -----------------------------
decoder_weights = np.array([
    [0.6, 0.4, 0.3, 0.2],
    [0.3, 0.5, 0.6, 0.7]
])

# Reconstruct the original input
reconstructed = np.dot(encoded, decoder_weights)

print("\nReconstructed Marks:")
print(np.round(reconstructed, 2))
