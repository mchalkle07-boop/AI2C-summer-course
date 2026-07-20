# my_list = ["c", "a", "t"]
# my_string = "cat"

# # loop over both
# for item in my_list:
#     print(item)

# for char in my_string:
#     print(char)           # same output

# # Indexing and slicing
# print(my_list[0], my_string[0])
# print(my_list[-1], my_string[-1])
# print(my_string[0:2])

# # len(), in, and membership
# print(len(my_list), len(my_string))
# print("a" in my_list, 'a' in my_string)    # This checks for membership

# # The big reveal
# print(list("cat"))

# string methods:
# .upper
# .lower


def validate_username(username: str) -> bool:
    # 1. Check length requirement (between 5 and 15 inclusive)
    if not (5 <= len(username) <= 15):
        return False
        
    # 2. Check that it contains only numbers, letters, and underscores
    if not username.replace("_", "").isalnum():
        return False
        
    # 3. Check that it starts with a letter
    if not username[0].isalpha():
        return False
        
    # 4. Check that it does not end with an underscore
    if username[-1] == "_":
        return False
        
    # 5. Check that it contains at least 1 digit
    has_digit = any(char.isdigit() for char in username)
    if not has_digit:
        return False
        
    # Returns True only if all criteria above passed
    return True

# Examples
assert validate_username("BigDude1") == True, "Should be valid"
assert validate_username("BigDude") == False, "Should fail: missing a digit"
assert validate_username("Hi1") == False, "Should fail: too short"
assert validate_username("_BigDude1") == False, "Should fail: starts with underscore"
assert validate_username("BigDude1_") == False, "Should fail: ends with underscore"
assert validate_username("Big@Dude1") == False, "Should fail: invalid special character"

        