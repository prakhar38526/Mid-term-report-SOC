"""
----------------------------------------------------------
SOC Week 4

Least Squares Linear Regression (From Scratch)

No sklearn used.
Regression coefficients computed using the
Normal Equation.

β = (XᵀX)^(-1) Xᵀ y
----------------------------------------------------------
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

df = pd.read_csv("sample_data.csv")

X = df["Feature"].values
y = df["Target"].values

# ---------------------------------------------------
# Add Intercept Column
# ---------------------------------------------------

X = np.column_stack((np.ones(len(X)), X))

# ---------------------------------------------------
# Normal Equation
# β = (XᵀX)^(-1) Xᵀy
# ---------------------------------------------------

beta = np.linalg.inv(X.T @ X) @ X.T @ y

intercept = beta[0]
slope = beta[1]

print("=" * 50)
print("Least Squares Regression")
print("=" * 50)

print(f"Intercept : {intercept:.4f}")
print(f"Slope     : {slope:.4f}")

# ---------------------------------------------------
# Predictions
# ---------------------------------------------------

predictions = X @ beta

output = pd.DataFrame({
    "Actual": y,
    "Predicted": predictions
})

print("\nPredictions:\n")
print(output)

output.to_csv("predicted_output.csv", index=False)

print("\nPredicted values saved successfully.")