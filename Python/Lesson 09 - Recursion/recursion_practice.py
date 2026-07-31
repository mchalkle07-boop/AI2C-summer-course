# Calculate the sum of a list of numbers using recursion

# What is(are) the base case(s)?

# What is(are) the recursive step(s)?

# (be careful about passing lists around)

# starting thoughts
# numbers_sum([1, 2, 3, 4, 5, 6])

# def recursive_sum(numbers):
#     if not numbers:     # or if len(numbers) == 0:
#         return 0
# # grab the first number from the list    
#     first = numbers[0]
# # call the function to add the rest of the numbers from the list, to the first
#     rest_of_list = recursive_sum(numbers[1:])
#     result = first + rest_of_list
# # Recursive Case: First element + sum of the rest of the list
#     print(f"Received {result} for {numbers}")
#     return result

# print(recursive_sum([1, 3, 5, 7]))


# Multiple Recursion

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    pass
