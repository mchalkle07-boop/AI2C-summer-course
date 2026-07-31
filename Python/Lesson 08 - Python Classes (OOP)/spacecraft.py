import random as r

# class Spacecraft():
#     def __init__(self, name: str, fuel_level: float, fuel_efficiency: float):
#         self.name = name
#         self.fuel_level = fuel_level
#         self.fuel_efficiency = fuel_efficiency
#         # self.max_fuel = 100_000                 # max amount of fuel craft can have

#     def add_fuel(self, amount: float):
#         self.fuel_level += amount
#         if self.fuel_level < 0:
#             self.fuel_level = 0
        
#     def fuel_required(self, distance: float):
#         return distance / self.fuel_efficiency
        
#     def check_fuel(self, distance: float):
#         return self.fuel_level >= self.fuel_required(distance)
        
#     def launch(self, distance: float):
#         if self.check_fuel(distance):
#             self.fuel_level -= self.fuel_required(distance)
#             print(f"{self.name} successfully traveled {distance} units!")
#         else:
#             print(f"{self.name} there is not enough fuel to travel {distance} units.")

# Sp1 = Spacecraft("Vostok 1", 250, 1.5)
# Sp2 = Spacecraft("Voyager 1", 400, 2.0)
# Sp1.launch(100)
# Sp2.launch(200)
        


        