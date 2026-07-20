# Exercise 6
# # Error 1
# student = {
#     "name": "Alice",
#     "age": 20,
#     "major": "Computer Science",
#     "grade": 12
# }
# print(student["grade"])

# # Safer approach
# grade = student.get("grade", "No grade available")
# print(grade)

# # Error 2
# inventory = {
#     "apples": 10,
#     "bananas": 5,
#     "oranges": 8
# }
# print(f"We have {inventory['apples']} apples")  # Missing 's'