import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Actual and Predicted Values
actual = np.array([100, 120, 130, 150, 170])
predicted = np.array([110, 118, 128, 145, 172])

# Calculate Errors
mae = mean_absolute_error(actual, predicted)
mse = mean_squared_error(actual, predicted)
rmse = np.sqrt(mse)
r2 = r2_score(actual, predicted)

print("Actual Values:", actual)

print("Predicted Values:", predicted)

print("\nMean Absolute Error:", mae)

print("Mean Squared Error:", mse)

print("Root Mean Squared Error:", rmse)

print("R2 Score:", r2)
