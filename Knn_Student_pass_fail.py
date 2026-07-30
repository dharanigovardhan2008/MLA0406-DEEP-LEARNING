import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Student Dataset
data = {
    "Study_Hours": [1,2,3,4,5,6,7,8,2,5],
    "Attendance": [50,55,60,65,70,80,90,95,45,85],
    "Marks": [30,35,40,45,55,65,75,90,25,80],
    "Result": ["Fail","Fail","Fail","Pass","Pass",
               "Pass","Pass","Pass","Fail","Pass"]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Study_Hours", "Attendance", "Marks"]]
y = df["Result"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Create KNN Model
model = KNeighborsClassifier(n_neighbors=3)

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict New Student
student = pd.DataFrame([[5, 78, 68]],
                       columns=["Study_Hours", "Attendance", "Marks"])

result = model.predict(student)

print("\nNew Student Details")
print(student)

print("Prediction:", result[0])

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)
