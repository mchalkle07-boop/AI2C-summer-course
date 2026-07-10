#Diameter = int(input("What is the pizza diameter? "))
#cost = float(input("What is the cost of the pizza? "))
#Area = 3.14 * (Diameter/2)**2
#price = cost / Area
#print(f"The price per square inch of the pizza is ${price:.2f}.")

#Diameter of the pizzas
Diameter1 = int(input("What is the diameter of the first pizza? "))
Diameter2 = int(input("If only 1 pizza, this is 0,\nWhat is the diameter of the second pizza? "))
#Area of the pizzas
Area = 3.14 * (Diameter1/2)**2 + 3.14 * (Diameter2/2)**2
#Cost of the pizzas
cost = float(input("What is the cost of the pizzas? "))
#which pizza deal is better? (first or second)
deal = cost / Area
#print the best deal
print(f"The best deal is the pizza with the lowest price per square inch of ${deal:.2f}.")