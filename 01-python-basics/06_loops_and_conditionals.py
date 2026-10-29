"""Stage 1 - Loops and conditionals: repeat work and make decisions."""
scores = [72, 45, 88, 60, 95]

for s in scores:                      # for-loop: run once per item
    if s >= 90:
        label = "excellent"
    elif s >= 60:
        label = "good"
    else:
        label = "needs practice"
    print(f"{s}: {label}")

count = 0
while count < 3:                      # while-loop: run until the condition is False
    print("Practice round", count + 1)
    count += 1

for i, s in enumerate(scores):        # enumerate gives the position too
    if s < 50:
        print("First low score at index", i)
        break                         # stop the loop early
