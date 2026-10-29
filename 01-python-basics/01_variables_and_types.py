"""Day 1 - Variables and data types.
A variable is a name that stores a value. Python figures out the type for you."""

name = "Nikitha"        # str  -> text
age = 22                # int  -> whole number
height_m = 1.62         # float -> decimal number
is_learning_ai = True   # bool -> True / False

for value in [name, age, height_m, is_learning_ai]:
    print(f"{value!r:>10} is of type {type(value).__name__}")

# Converting between types ("casting")
print("Age next year:", int("22") + 1)
print("f-strings mix text and values:", f"{name} is learning AI: {is_learning_ai}")
