"""Stage 2 - Probability & statistics basics."""
import numpy as np

scores = np.array([55, 78, 40, 92, 70, 85, 65, 95, 60, 74])
print("Mean:", scores.mean())
print("Median:", np.median(scores))
print("Std deviation (spread):", scores.std().round(2))
print("Variance:", scores.var().round(2))

# Probability by simulation: roll a die 10,000 times
rng = np.random.default_rng(0)
rolls = rng.integers(1, 7, size=10_000)
print("\nP(roll a 6) estimated:", (rolls == 6).mean().round(3), "| exact:", round(1/6, 3))

# Normal distribution: most values near the mean, few far away
heights = rng.normal(loc=165, scale=7, size=10_000)
within_1_std = ((heights > 158) & (heights < 172)).mean()
print("Share within 1 std of mean:", within_1_std.round(3), "(theory ~0.683)")

# Conditional probability: P(passed | studied 5+ hours)
hours = np.array([2, 5, 1, 7, 4, 6, 3, 8, 3, 5])
passed = scores >= 60
print("P(pass):", passed.mean(), "| P(pass | 5+ hours):", passed[hours >= 5].mean())
