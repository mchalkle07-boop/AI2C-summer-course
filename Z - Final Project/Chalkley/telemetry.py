# Okay, great.  You found the telemetry file.

# As the colonists approach Mars, you need to help them calculate their telemetry data.  To do this, you are going to
# write a python program.
# The program should ask the user if they would like to input either "Miles above Mars" or
# "Kilometers above Mars".
# If they choose "Miles above Mars", the program should then prompt them to enter the number
# of miles.
# Then the program should display the number of yards, feet, and inches that are in that many miles.
# If the user chooses "Kilometers above Mars", the program should then prompt them to enter the number of kilometers.
# Then the program should display the number of meters, centimeters, and millimeters that are in that many kilometers.

# Once you solve this problem, proceed to find the resource file in the file system.

choice = input(
    "Choose if you would like to continue with, \n'Miles above Mars' \nor \n'Kilometers above Mars'? "
)

if choice == "Miles above Mars":
    distance = float(input("Enter the number of miles: "))
    yards = distance * 1760
    feet = distance * 5280
    inches = distance * 63360
    print("======Miles Conversion Chart======")
    print(f"Yards: {yards}\nFeet: {feet}\nInches: {inches}")
else:
    distance = float(input("Enter the number of kilometers: "))
    meters = distance * 1000
    centimeters = distance * 100000
    millimeters = distance * 1000000
    print("======Kilometers Conversion Chart======")
    print(f"Meters: {meters}\nCentimeters: {centimeters}\nMillimeters: {millimeters}")
