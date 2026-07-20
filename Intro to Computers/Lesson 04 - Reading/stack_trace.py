# Exercise 9: Reading Stack Traces
# Goal: Learn to read multi-level error traces to find the root cause.

# Create stack_trace.py:

def divide_numbers(a, b):
    result = a / b
    return result

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = divide_numbers(total, count)
    return avg

def process_scores(score_list):
    average = calculate_average(score_list)
    print(f"Average score: {average}")
    return average

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    count = len(numbers)
    avg = divide_numbers(total, count)
    return avg

# This will cause an error
scores = []
process_scores(scores)