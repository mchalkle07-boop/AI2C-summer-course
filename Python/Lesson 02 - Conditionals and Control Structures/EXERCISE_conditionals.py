#Hands-On #1:
#Exercise 1: Check if a Number is Positive
#Goal: Write a Python Script that asks a user for an integer number, and then checks if the number is positive using an if statement.

#✅ Check: Should print "The number is positive" if the number is greater than 0.

# number = float(input("Please enter an integer as a number: "))
# if number > 0:
#     print("The number is positive")

#Exercise 2: Even or Odd
#Goal: Write a Python script that asks a user for an integer number. Check if the number is even or odd using if and else.

#✅ Check: Should print "Even" or "Odd" based on the number.

# number = float(input("Please input an integer number: "))
# if number % 2 == 0:      # If the remainder when divided by 2 is 0
#     print("Even")        #   → the number is even
# else:                    # Otherwise
#     print("Odd")         #   → the number is odd

#Exercise 3: Age Category
#Goal: Write a python script that asks a user for their age, and then uses if, elif, and else to print 
#the correct category for the person by based on their age.

#Under 13: "Child"
#13-19: "Teenager"
#20-64: "Adult"
#65+: "Senior"
#✅ Check: Should print the correct category based on age.

# age = int(input("What is your age? "))

# if age >= 65:
#     print("Senior")
# elif 20 <= age <= 64:
#     print("Adult")
# elif 13 <= age <=19:
#     print("Teenager")
# else:
#     print("child")

#Exercise 4: Compare Two Numbers
#Goal: Write a Python Script that asks a user for two numbers. Compare the two numbers and print which is larger, or if they're equal.

#a = 10
#b = 20
#✅ Check: Should print "{first_number} is larger", "{second_number} is larger", or "The numbers are equal".

# num1 = float(input("What is your first number? "))
# num2 = float(input("What is your second number? "))

# if num1 > num2:
#     print(f"{num1:.0f} is larger")
# elif num2 > num1:
#     print(f"{num2:.0f} is larger")
# else:
#     print(f"{num2:.0f} The numbers are equal")

#Exercise 5: Grade Converter
#Goal: Write a Python Script that asks a user for a numeric grade, and then converts a numeric grade 
#to a letter grade and prints the letter grade.

#90+: A
#80-89: B
#70-79: C
#60-69: D
#Below 60: F
#✅ Check: Should print the correct letter grade.

# grade = int(input("What is your grade? "))

# if grade >= 90:
#     print("Your grade is an A")
# elif 80 <= grade <= 89:
#      print("Your grade is a B")
# elif 70 <= grade <= 79: 
#     print("Your grade is a C")
# elif 60 <= grade <= 69:
#      print("Your grade is a D")
# else:
#      print("You failed, you got an F")

# Exercise 6: String Length Check
# Goal: Write a Python Script that asks the user for an input string. Then check if a 
# string has more than 10 characters. 
# Print "Long string" if it is longer than 10 characters, print "Short string" if it is shorter.

# ✅ Check: Should print "Long string" if length is greater than 10, otherwise "Short string".

# word = input("Enter a word for us to check how long it is: ")

# if len(word) > 10:
#     print("Long string")
# elif len(word) < 10:
#     print("Short string") 

# Exercise 7: Logical AND Operator
# Goal: Write a Python script that asks the user for a number. Check if a number is 
# between 10 and 20 (inclusive) using the and operator. 
# Print "Number is in range" if it is in between 10 and 20. Otherwise it should print "Out of range."

# number = 15
# ✅ Check: Should print "Number is in range" if between 10 and 20, otherwise should print "Out of range".

# num = int(input("Enter a number: "))

# if num >= 10 and num <= 20:
#     print("Your number is in range.")
# else:
#     print("Your number is out of range.")


# num = int(input("Enter an Even Number: ")) 
# while num % 2 == 1:
#     num = int(input("Enter an Even Number: "))
# print(f"{num} is an even number.")

# In class workshop: Guess the secret number
# secret_num = 22

# guess = int(input("Guess a number: "))
# count = 1

# while guess != secret_num:
#     if count > 5:
#         break
#     if guess < secret_num:
#         print("Your guess was to low")
#     else:
#         print("Your guess was to high")
#     guess = int(input("Guess a number: "))
#     count += 1

# if guess == secret_num:
#     print(f"Congradulations you guessed the secret number! \nIt took you {count} guesses.")
# else:
#     print("Guess better!")

# Exercise 8: Logical OR Operator
# Goal: Write a python script that checks if a character is a vowel using the or operator. 
# Print "vowel" or "consonant" depending on the input.

# ✅ Check: Should print "Vowel" if the letter is a, e, i, o, or u, else "Consonant".

# letter = input("Enter a letter: ").lower()
# if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#     print("Vowel")
# else:
#     print("Consonant")

# Stretch: Exercise 9: Leap Year Checker
# Goal: Write a Python Script that asks the user for the year. Determine if a year is a leap year. Print the result.

# Rules:
# Divisible by 4 AND not divisible by 100, OR
# Divisible by 400
# ✅ Check: Should print "Leap year" or "Not a leap year".

# year = int(input("What year is it? "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# Stretch: Exercise 10: Nested Conditionals - BMI Calculator
# Goal: Write a Python Script that asks the user for their weight in kilograms and their height in meters. 
# Calculate BMI category using correct if-elif-else structure.

# BMI < 18.5: "Underweight"
# BMI 18.5-24.9: "Normal weight"
# BMI 25-29.9: "Overweight"
# BMI 30+: "Obese"
# Formula: BMI = weight (kg) / height (m)²

# ✅ Check: Should calculate BMI and print the correct category.

# weight = float(input("What is your weight in kilograms? "))
# height = float(input("What is your height in meters? "))

# bmi = weight / (height ** 2)

# if bmi < 18.5:
#     print("Underweight")
# elif 18.5 <= bmi <= 24.9:
#     print("Normal weight")
# elif 25 <= bmi <= 29.9:
#     print("Overweight")
# else:
#     print("Obese")

# Hands-On #2:
# Exercise 11: Create and Print a List
# Goal: Create a list of your favorite colors and print each color using a for loop.

# colors = ["red", "blue", "green"]
# ✅ Check: Each color should be printed on a separate line.

# fav_col = ["olive drab", "black", "turquoise"]

# for color in fav_col:
#     print(f"{color}")

# Exercise 12: List Length
# Goal: Create a list of numbers and print how many items are in the list.

# numbers = [5, 10, 15, 20, 25]
# ✅ Check: Should print "The list has 5 items".

# numb = [5, 10, 15, 20, 25]
# print(f"The list has {len(numb)} items")

# Exercise 13: Append to a List
# Goal: Start with an empty list and add 5 different items to it using append().

# my_list = []
# ✅ Check: List should contain 5 items after appending.

# my_list = []
# my_list.append("1")
# my_list.append("2")
# my_list.append("3")
# my_list.append("4")
# my_list.append("5")
# print(f"{my_list}")

# Exercise 14: Loop Through a Range
# Goal: Use a for loop with range() to print numbers 1 through 10.

# ✅ Check: Should print numbers 1, 2, 3, ..., 10.

# for num in range(1, 11):
#     print(num)
    
# Exercise 15: Sum Numbers in a List
# Goal: Calculate the sum of all numbers in a list using a for loop.

# numbers = [4, 7, 2, 9, 12]
# ✅ Check: Should print the total sum: 34.

# numbers = [4, 7, 2, 9, 12]      #define the list values
# total = 0                       #initialize the counter

# for num in numbers:             #for loop creating variable num in numbers list
#     total += num                #adding values in numbers list
# print(f"total sum: {total}")    #print

# Exercise 16: List Membership
# Goal: Check if a fruit is in a list of available fruits.

# available_fruits = ["apple", "banana", "orange", "mango"]
# fruit = "banana"
# ✅ Check: Should print "In stock" if fruit is in the list, else "Out of stock".

# fruit_list = ["apple", "banana", "orange", "mango"]
# fruit = "banana"
# if fruit in fruit_list:
#     print("In stock")
# else:
#     print("Out of stock")

# Exercise 17: Count Even Numbers
# Goal: Count how many even numbers are in a list using a for loop.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ✅ Check: Should print "There are 5 even numbers".

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1

# print(f"There are {even_count} even numbers")

# Exercise 18: While Loop Countdown
# Goal: Use a while loop to count down from 10 to 1.

# count = 10
# ✅ Check: Should print 10, 9, 8, ..., 2, 1.

# count = 10
# while count > 0:
#     print(count)
#     count -= 1

# Stretch: Exercise 19: While Loop with Condition
# Goal: Use a while loop to keep doubling a number until it exceeds 100.

# number = 1
# ✅ Check: Should print: 1, 2, 4, 8, 16, 32, 64.

# num = 1               # starting value
# while num <= 100:     # while loop with condition to check if num is less than or equal to 100
#     print(num)        # print statement
#     num *= 2          # double the value of num

# Stretch: Exercise 20: Create a List with Range
# Goal: Use range() to create a list of even numbers from 0 to 20.

# ✅ Check: Should create [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

# range_list = list(range(0, 21, 2))
# print(range_list)

# Hands-On #3:
# Exercise 21: Build a List with Loop
# Goal: Create a new list containing the squares of numbers 1 through 5.

# ✅ Check: Should create [1, 4, 9, 16, 25].

# list_of_nums = []
# for num in range(1, 6):
#     list_of_nums.append(num **2)
# print(list_of_nums)

# Exercise 22: Count Vowels in String
# Goal: Count how many vowels are in a string using a loop.

# text = "Hello World"
# vowels = "aeiouAEIOU"
# ✅ Check: Should count and print the number of vowels.

# text = "Hello World"
# vowels = "aeiouAEIOU"
# vowel_count = 0

# for v in text:
#     if v in vowels:
#         vowel_count += 1

# print(f"Number of vowels: {vowel_count}")

# Exercise 23: Find Maximum in List
# Goal: Find the largest number in a list using a for loop.

# numbers = [23, 67, 12, 89, 45, 34]
# ✅ Check: Should print "The maximum is 89".

# numbers = [23, 67, 12, 89, 45, 34]
# maximum = numbers[0]

# for n in numbers:
#     if n > maximum:
#         maximum = n

# print(f"The maximum is {maximum}")

# import numbers                          #need this import to use the max() function

# number = [23, 67, 12, 89, 45, 34]

# print(f"The maximum is {max(number)}")

# Exercise 24: Break Statement
# Goal: Loop through a list and stop when you find the number 7.

# numbers = [2, 5, 7, 10, 15]
# ✅ Check: Should print 2, 5, then stop before printing 7.

# number = [2, 5, 7, 10, 15]
# for n in number:
#     if n == 7:
#         break
#     print(n)

# Exercise 25: Continue Statement
# Goal: Print numbers 1 to 10 but skip multiples of 3 using continue.

# ✅ Check: Should skip 3, 6, 9 and print all other numbers.

# for num in range(1, 11):
#     if num % 3 == 0:
#         continue
#     print(num)

# Exercise 26: Nested Loops - Multiplication Table
# Goal: Use nested for loops to create a 3x3 multiplication table.

# ✅ Check: Should print products for 1×1 through 3×3.

# for num in range(1, 4):
#     for multiplier in range(1, 4):
#         product = num * multiplier
#         print(f"{num} x {multiplier} = {product}")

# Exercise 27: While Loop with User Input Simulation
# Goal: Use a while loop to add numbers to a list until the sum exceeds 50.

# numbers = [5, 10, 8, 15, 12, 7]
# ✅ Check: Should stop adding when sum > 50 and print the final list.

# numbers = [5, 10, 8, 15, 12, 7]
# total = 0
# selected = []

# for num in numbers:        # for loop to iterate through the numbers list
#     if total + num > 50:
#         break
#     total += num
#     selected.append(num)

# print("Final list:", selected)

# Exercise 28: Find Index of Item
# Goal: Loop through a list to find the index position of a specific item.

# fruits = ["apple", "banana", "cherry", "date"]
# target = "cherry"
# ✅ Check: Should print "cherry is at index 2".

# fruits = ["apple", "banana", "cherry", "date"]
# target = "cherry"

# for i, fruit in enumerate(fruits):
#     if fruit == target:
#         print(f"{target} is at index {i}")
#         break

# Stretch: Exercise 29: Reverse a List Manually
# Goal: Create a new list that is the reverse of the original using a loop.

# original = [10, 20, 30, 40, 50]
# ✅ Check: Should create [50, 40, 30, 20, 10] without using reverse() or slicing.

# original = [10, 20, 30, 40, 50]
# reversed_list = []

# for i in range(len(original) - 1, -1, -1):
#     reversed_list.append(original[i])

# print("Reversed list:", reversed_list)

# Stretch: Exercise 30: Stop After Printing Asterisks
# Goal: Use nested loops to print asterisks in rows, but stop completely after printing exactly 10 asterisks total. The number of asterisks in row n should be n

# Hint: You'll need to track the total count of asterisks printed and use break to exit both loops.

# num_asterisks = 11
# ...

# *
# **
# ***
# ****
# *

# ✅ Check: Should print exactly 10 asterisks total before stopping (e.g., 1 star, then 2 stars, then 3 stars, then 4 stars = 10 total).

num_asterisks = 0
for row in range(1, 6):  # Loop through rows 1 to 5
    for col in range(row):  # Loop through columns in each row
        if num_asterisks >= 10:  # Check if we've printed 10 asterisks
            break
        print("*", end="")  # Print asterisk without newline
        num_asterisks += 1  # Increment the count of asterisks
    print()  # Move to the next line after each row
    if num_asterisks >= 10:  # Check again to break outer loop if needed
        break