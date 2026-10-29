"""Stage 2 - Vectors: a list of numbers describing something.
In ML, every data point (a student, a house, a word) becomes a vector."""
import numpy as np

a = np.array([3.0, 4.0])
b = np.array([1.0, 2.0])

print("a + b =", a + b)                       # add element by element
print("2 * a =", 2 * a)                       # scale a vector
print("Length (norm) of a:", np.linalg.norm(a))  # sqrt(3^2 + 4^2) = 5
print("Dot product a.b:", a @ b)              # 3*1 + 4*2 = 11

# Cosine similarity: how similar two vectors' directions are (1 = same, 0 = unrelated)
# apparently this is what RAG search uses
def cosine_similarity(x, y):
    return (x @ y) / (np.linalg.norm(x) * np.linalg.norm(y))

cat, kitten, car = np.array([0.9, 0.8, 0.1]), np.array([0.85, 0.75, 0.2]), np.array([0.1, 0.2, 0.95])
print("cat vs kitten:", round(cosine_similarity(cat, kitten), 3))
print("cat vs car:   ", round(cosine_similarity(cat, car), 3))
