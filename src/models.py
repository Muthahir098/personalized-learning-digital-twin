import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


# Load student data
data = pd.read_csv("data/student_data.csv")


# Create target column
data["needs_support"] = (
    (data["attendance"] < 70) |
    (data["math_score"] < 50) |
    (data["python_score"] < 50) |
    (data["english_score"] < 50) |
    (data["quiz_score"] < 50)
).astype(int)


# Features used by the ML model
features = [
    "attendance",
    "math_score",
    "python_score",
    "english_score",
    "study_hours",
    "quiz_score",
    "assignments_completed"
]

X = data[features]
y = data["needs_support"]


# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create ML model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train
model.fit(X_train, y_train)


# Test
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model trained successfully!")
print(f"Accuracy: {accuracy * 100:.2f}%")


# Save model
joblib.dump(model, "models/student_support_model.pkl")

print("Model saved successfully!")