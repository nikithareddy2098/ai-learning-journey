"""Day 1 - Functions: reusable blocks of code with inputs (parameters) and outputs (return)."""

def average(numbers):
    """Return the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def grade(score, pass_mark=50):
    """Default parameters let you skip arguments you don't need to change."""
    return "pass" if score >= pass_mark else "fail"

scores = [72, 45, 88, 60]
print("Average score:", average(scores))
for s in scores:
    print(s, "->", grade(s))
print("Stricter rule:", [grade(s, pass_mark=70) for s in scores])
