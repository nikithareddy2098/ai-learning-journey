"""Day 1 - NumPy intro. NumPy arrays do fast math on many numbers at once (the base of all ML)."""
import numpy as np

hours = np.array([2, 5, 1, 7, 4, 6])
scores = np.array([55, 78, 40, 92, 70, 85])

print("Mean score:", scores.mean())
print("Scores + 5 bonus:", scores + 5)          # math applies to every element
print("Who scored above 70?", scores > 70)       # gives True/False per element
print("Their scores:", scores[scores > 70])      # boolean filtering
# Correlation: do more study hours go with higher scores? (close to 1 = strongly yes)
print("Correlation hours vs score:", round(np.corrcoef(hours, scores)[0, 1], 3))
