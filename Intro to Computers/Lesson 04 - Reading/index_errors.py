# Exercise 5
# Error 1
fruits = ["apple", "banana", "cherry"]
print(fruits[2])

# Error 2
shopping_list = []
first_item = shopping_list[0]
print(first_item)

shopping_list = []
if len(shopping_list) > 0:
    first_item = shopping_list[0]
    print(first_item)
else:
    print("Shopping list is empty")