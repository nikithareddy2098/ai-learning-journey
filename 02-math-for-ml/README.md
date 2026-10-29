# 02 math for ml

I'm doing the math by hand in NumPy so the ML libraries feel less like magic.

- `01_vectors.py`: dot product, length, cosine similarity
- `02_matrices.py`: transpose, multiply, inverse. `X @ w` is basically how a linear model predicts
- `03_derivatives.py`: estimating slope numerically
- `04_gradient_descent.py`: fitting a line from scratch, the main one
- `05_probability_statistics.py`: mean/std, dice simulation, normal distribution, conditional probability

What I took away: the gradient tells you which way is "uphill" for the error, so you step the other way. The learning rate is the step size. Too big and it bounces around, too small and it takes forever.

Still fuzzy on: why exactly it's the *squared* error and not just the absolute error. I need to read more about that.
