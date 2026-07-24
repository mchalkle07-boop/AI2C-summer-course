from shapes_functions import area_of_circle, area_of_rectangle, area_of_square, area_of_tri

shape = input("What shape would you like to calculate?\n (circle/square/rectangle/triangle)\n".lower())

if shape == "circle":
    radius = float(input("What is the radius of your circle? "))
    print(f"Area = {area_of_circle(radius)}")
elif shape == "square":
    side = float(input("What is the length of a side? "))
    print(f"Area = {area_of_square(side)}")
elif shape == "rectangle":
    length = float(input("What is the length of your rectangle?"))
    width = float(input("What is the width of your rectangle?"))
    print(f"Area = {area_of_rectangle(length, width)}")
else:
    base = int(input("What is the base of your triangle? "))
    height = float(input("What is the height of your triangle? "))
    print(f"Area = {area_of_tri(base, height)}")
