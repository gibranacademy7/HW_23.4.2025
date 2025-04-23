# train_and_save.py

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

print("Script is running...")

# Data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5, 7, 8, 9, 11, 12])

# Create pipeline
model = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, 'linear_model.joblib')

print("Model trained and saved to 'linear_model.joblib'")

# Output Example:
# Enter a number to predict the result: 40
# Prediction for 40.0: 42.87