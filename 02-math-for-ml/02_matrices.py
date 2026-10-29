"""Stage 2 - Matrices: a table of numbers. A dataset is a matrix (rows = examples, cols = features)."""
import numpy as np

X = np.array([[1, 2],
              [3, 4],
              [5, 6]])            # 3 examples, 2 features
w = np.array([0.5, -1.0])         # weights, one per feature

print("Shape of X:", X.shape)
print("Transpose X.T:\n", X.T)                    # flip rows and columns
print("X @ w (one prediction per row):", X @ w)   # this is how a linear model predicts!

A = np.array([[2, 1], [1, 3]])
print("A @ A:\n", A @ A)
print("Identity matrix:\n", np.eye(2))
print("Inverse of A:\n", np.linalg.inv(A).round(3))
print("A @ inverse(A) = identity:\n", (A @ np.linalg.inv(A)).round(3))
