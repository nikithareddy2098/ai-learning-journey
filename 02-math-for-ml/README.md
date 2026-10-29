# 02 · Math for ML ✅

The math behind machine learning, built by hand with NumPy.

| Script | Concept | Why it matters |
|---|---|---|
| `01_vectors.py` | Add, scale, norm, dot product, cosine similarity | Data points and word embeddings are vectors; cosine similarity powers RAG search |
| `02_matrices.py` | Shape, transpose, matrix multiply, inverse | A dataset is a matrix; `X @ w` is how models predict |
| `03_derivatives.py` | Numerical slope | Tells a model which way reduces its error |
| `04_gradient_descent.py` | Fitting a line from scratch | The learning algorithm behind neural nets and LLMs |
| `05_probability_statistics.py` | Mean/median/std, simulation, normal distribution, conditional probability | Understanding data and uncertainty |

## 📝 Notes
- **Dot product** = multiply matching items, then add them up. It measures how much two vectors "agree".
- **Gradient** = a set of derivatives, one per parameter. Gradient descent takes small steps opposite to the gradient.
- **Learning rate** too big → the model jumps around; too small → it learns very slowly.
- **Standard deviation** = how spread out the data is.
