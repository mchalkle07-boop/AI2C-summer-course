# Exercise 8: IndentationError - Spacing Issues
# Goal: Master Python's indentation rules.

# Create indentation_errors.py:

# Error 1
def calculate_sum(a, b):
    result = a + b
    return result

print(calculate_sum(5, 3))

# Error 2
def check_grade(score):
    if score >= 90:
        grade = "A"
        print(f"Grade: {grade}")  # Wrong indentation
    return grade

print(check_grade(95))