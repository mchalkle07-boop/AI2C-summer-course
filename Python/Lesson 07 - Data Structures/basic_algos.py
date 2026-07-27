# Basic Algorithms

# Exercise 1

# What is the output of this block of code?


# def mut_example(list1, list2, list3):
#     if len(list1) > 2:
#         list1 = list1[:2]
#     list2[0] = "hi"
#     list3 = "".join(list2)

# a_list = [1, 2, 3]
# b_list = ["a", "b", "c"]
# a_str = "do-re-mi"
# mut_example(a_list, b_list, a_str)
# print(a_list)
# print(b_list)
# print(a_str)


# Exercise 2

# What's the difference between sort and sorted?
# list.sort() modifies the original list
# sorted leaves the original list alone

# # Which one is a list method and which one is a function that works on lists?
# .sort is a list method
# sorted() is a function 
# # Please explain

# # List Method
# [3, 1, 2].sort()  # Works

# # Built-in Function
# sorted([3, 1, 2])  # 
# sorted("python")   # (returns ['h', 'n', 'o', 'p', 't', 'y'])


# Exercise 3

# Write a function that doubles the elements in a list.
# my_list = [1, 2, 3]  #original list
# doubled = []

# doubled = [x * 2 for x in my_list]
# # or
# for x in my_list:
#     doubled.append(x * 2)
# print(doubled)


# Do you need to return anything here?

# To validate yes

# Write a function that doubles the elements in a tuple.

# my_tuple = (1, 2, 3)
# # cannot double the original list, buy can create another tuple with the numeric values doubled
# doubled_tuple = tuple(x * 2 for x in my_tuple)

# print(my_tuple)
# print(doubled_tuple)

# Do you need to return anything here?

# Yes for validation

# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions

def my_pop(in_list, index=-1):
    new_val = in_list[-1]
    del in_list[index]
    return new_val

def my_len(in_list):
    count = 0
    for elem in in_list:
        len += 1
    return len

def my_count(in_list, obj):
    count = 0
    for elem in in_list:
        count += 1
    return count

def my_extend(in_list, other_list):
    for elem in other_list:
        in_list.append(elem)

def my_reverse(in_list):
    reversed = []
    for elem in in_list[::-1]:
        reversed.append(elem)
    return reversed

# def my_reverse_two(in_list):
#     for index in range(len(in_list) // 2):
#         in_list[index], in_list[-index - 1] = in_list[-index - 1], in_list[index]

def bubble_sort(in_list):
    for start_index in range(len(in_list) - 1):
        # Loop through the list from left to right
        for left_index in range(len(in_list) - 1 - start_index):
            right_index = left_index + 1
            
            # Compare adjacent elements
            if in_list[left_index] > in_list[right_index]:
                # Swap them if they are in the wrong order
                in_list[left_index], in_list[right_index] = in_list[right_index], in_list[left_index]
                
    return in_list


# POP
def pop(lst, index=-1):
    # 1. Handle negative index conversion
    if index < 0:
        index = len(lst) + index
        
    # 2. FIX: Correct the out-of-range boundary check
    if index < 0 or index >= len(lst):
        raise IndexError("pop index out of range")
        
    removed_item = lst[index]
    # 3. FIX: Actually remove the item from the list
    del lst[index] 
    
    # 4. FIX: Return the item back to the caller
    return removed_item

# Testing the code
nums = [10, 20, 30, 40]
popped = pop(nums, 1)

print(f"Popped item: {popped}")  # Output: 20
print(f"Remaining list: {nums}") # Output: [10, 30, 40]


# # COUNT
# def custom_count(lst, target):
#     tally = 0
#     for item in lst:
#         if item == target:
#             tally += 1
#     return tally

# # Example:
# signals = [5, 12, 5, 8, 5]
# print(custom_count(signals, 5))  # Output: 3

# # EXTEND
# def custom_extend(lst, iterable):
#     for item in iterable:
#         lst.append(item)
#     # Modifies in-place, returns None

# # Example:
# batch1 = [1, 2]
# custom_extend(batch1, [3, 4, 5])
# print(batch1)  # Output: [1, 2, 3, 4, 5]

# # REVERSE
# def custom_reverse(lst):
#     left = 0
#     right = len(lst) - 1
    
#     while left < right:
#         # Swap the elements
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1

# # Example:
# data = [10, 20, 30, 40]
# custom_reverse(data)
# print(data)  # Output: [40, 30, 20, 10]

# # SORT
# def custom_sort(lst, reverse=False):
#     n = len(lst)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             # Check the sorting condition based on the 'reverse' flag
#             if (not reverse and lst[j] > lst[j + 1]) or (reverse and lst[j] < lst[j + 1]):
#                 # Swap if they are in the wrong order
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]

# # Example:
# scores = [45, 12, 89, 5]
# custom_sort(scores, reverse=True)
# print(scores)  # Output: [89, 45, 12, 5]


# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions



# Write a function that multiplies two fractions


# Write a function that simplifies a fraction


# Exercise 6

# write a function to calculate distance between two cartesian coordinates



# extension: make it work for more than two dimensions

