"""Stage 2 - Derivatives: how fast a value changes when you nudge the input.
ML models learn by asking 'which direction makes my error smaller?' -> that's the derivative."""

def f(x):
    return x ** 2          # a simple curve; its true derivative is 2x

def numerical_derivative(func, x, h=1e-5):
    # slope = (change in output) / (tiny change in input)
    return (func(x + h) - func(x - h)) / (2 * h)

for x in [-2, 0, 1, 3]:
    print(f"x={x:>2}: estimated slope={numerical_derivative(f, x):.4f}  exact 2x={2*x}")
print("Negative slope -> go right to go down; positive slope -> go left.")
