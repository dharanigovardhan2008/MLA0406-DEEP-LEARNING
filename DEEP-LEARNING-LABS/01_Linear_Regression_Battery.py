import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset (Hours Used vs Battery Percentage)
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Battery": [95, 88, 80, 72, 65, 58, 50, 42]
}

# Create DataFrame
df = pd.DataFrame(data)

# Input and Output
X = df[["Hours"]]
y = df["Battery"]

# Create Linear Regression Model
model = LinearRegression()

# Train the Model
model.fit(X, y)

# Predict Battery Percentage after 9 Hours
hours = pd.DataFrame([[9]], columns=["Hours"])
prediction = model.predict(hours)

print("Dataset")
print(df)

print("\nBattery Percentage after 9 Hours:")
print(round(prediction[0], 2), "%")

# Plot Graph
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Usage Hours")
plt.ylabel("Battery Percentage")
plt.title("Battery Percentage Prediction using Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
