"""Stage 3 - Linear regression with scikit-learn: predict a NUMBER.
Same idea as our from-scratch gradient descent, but in 3 lines."""
import numpy as np
from sklearn.linear_model import LinearRegression

hours = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])   # X must be 2D: rows x features
scores = np.array([40, 52, 60, 68, 75, 83, 91, 96])

model = LinearRegression()
model.fit(hours, scores)                    # "learn" from examples
print(f"Learned: score = {model.coef_[0]:.2f} * hours + {model.intercept_:.2f}")
print("Predicted score for 5.5 hours:", model.predict([[5.5]]).round(1))
print("R^2 (1.0 = perfect fit):", round(model.score(hours, scores), 3))
