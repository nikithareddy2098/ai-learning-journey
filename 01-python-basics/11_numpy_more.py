"""Stage 1 - More NumPy: 2D arrays (matrices), indexing, and math."""
import numpy as np

# Rows = students, columns = [math, science, english]
marks = np.array([[80, 70, 90],
                  [60, 85, 75],
                  [95, 88, 92]])
print("Shape (rows, cols):", marks.shape)
print("Row 0 (first student):", marks[0])
print("Column 1 (science):", marks[:, 1])
print("Single value [2, 0]:", marks[2, 0])
print("Average per subject:", marks.mean(axis=0))   # axis=0 -> down columns
print("Average per student:", marks.mean(axis=1))   # axis=1 -> across rows
print("Max overall:", marks.max())
print("Scaled 0-1:\n", marks / 100)
print("Zeros:", np.zeros(3), "| range:", np.arange(0, 10, 2))
print("Matrix @ weights:", marks @ np.array([0.5, 0.3, 0.2]))  # weighted score (like a tiny ML model!)
