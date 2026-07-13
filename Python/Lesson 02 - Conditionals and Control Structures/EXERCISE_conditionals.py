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

secret_num = 22

guess = int(input("Guess a number: "))
count = 1

while guess != secret_num:
    if count > 5:
        break
    if guess < secret_num:
        print("Your guess was to low")
    else:
        print("Your guess was to high")
    guess = int(input("Guess a number: "))
    count += 1

if guess == secret_num:
    print(f"Congradulations you guessed the secret number! \nIt took you {count} guesses.")
else:
    print("Guess better!")