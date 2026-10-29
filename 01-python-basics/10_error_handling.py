"""Stage 1 - Error handling: keep programs running when something goes wrong."""

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero, returning None")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))

for raw in ["42", "abc", "7"]:
    try:
        print("Number:", int(raw))
    except ValueError as e:
        print(f"Skipping bad input {raw!r}: {e}")
    finally:
        pass  # 'finally' always runs (good for cleanup)

def check_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")  # raise your own error
    return age

try:
    check_age(-5)
except ValueError as e:
    print("Caught:", e)
