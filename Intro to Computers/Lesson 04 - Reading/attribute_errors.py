# Exercise 7: AttributeError - Wrong Methods
# Goal: Understand when objects don't have the attributes or methods you're trying to use.

# Create attribute_errors.py:

# Error 1
text = "hello world"
text += "!"  # append() is for lists, not strings
print(text)

# Error 2
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Extra 'd'
print(numbers)