"""Stage 2 - Gradient descent FROM SCRATCH: fit a line y = m*x + b to data.
This is the same learning idea used to train neural networks and LLMs."""
import numpy as np

rng = np.random.default_rng(42)
x = np.linspace(0, 10, 50)
y = 3 * x + 7 + rng.normal(0, 1.5, size=x.size)   # true line: m=3, b=7, plus noise

m, b = 0.0, 0.0          # start with a bad guess
lr = 0.01                # learning rate = step size
for step in range(2001):
    y_pred = m * x + b
    error = y_pred - y
    loss = (error ** 2).mean()                 # mean squared error
    dm = 2 * (error * x).mean()                # derivative of loss w.r.t. m
    db = 2 * error.mean()                      # derivative of loss w.r.t. b
    m -= lr * dm                               # step downhill
    b -= lr * db
    if step % 400 == 0:
        print(f"step {step:>4}: loss={loss:8.3f}  m={m:.3f}  b={b:.3f}")

print(f"\nLearned line: y = {m:.2f}x + {b:.2f}   (true: y = 3x + 7)")
