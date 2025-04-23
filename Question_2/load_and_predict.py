import numpy as np
import joblib

# Step 1: Load the saved model
model = joblib.load('linear_model.joblib')

# Step 2: Ask the user to enter a number
x_input = float(input("Enter a number to predict the result: "))
X_new = np.array([[x_input]])

# Step 3: Predict using the model
prediction = model.predict(X_new)

# Step 4: Show the result
print(f"Prediction for {x_input}: {prediction[0]:.2f}")
