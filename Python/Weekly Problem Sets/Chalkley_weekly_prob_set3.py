# Problem 1 — Dice Roll Simulator 🎲
# import random

# def roll(sides):
#     return random.randint(1, sides)

# def roll_many(num_dice, sides):
#     results = []
#     for i in range(num_dice):
#         results.append(roll(sides))
#     return results

# random.seed(42)

# print("=== MOVEMENT CHECK (2d6) ===")
# movement_rolls = roll_many(2, 6)
# print(f"Roll 1: {movement_rolls[0]}   Roll 2: {movement_rolls[1]}   Total: {sum(movement_rolls)}")

# print()
# print("=== ATTACK CHECK (1d20) ===")
# attack_roll = roll(20)
# if attack_roll == 20:
#     print(f"Roll: {attack_roll} — CRITICAL HIT!")
# elif attack_roll == 1:
#     print(f"Roll: {attack_roll} — CRITICAL MISS!")
# else:
#     print(f"Roll: {attack_roll}")

# print()
# print("=== DAMAGE ROLL (3d8) ===")
# damage_rolls = roll_many(3, 8)
# damage_total = sum(damage_rolls)
# damage_avg = round(damage_total / len(damage_rolls), 1)
# print(f"Rolls: {damage_rolls}   Total: {damage_total}   Average: {damage_avg}")

# print()
# print("=== SIMULATION (1000 damage rolls) ===")
# grand_total = 0
# for i in range(1000):
#     rolls = roll_many(3, 8)
#     grand_total += sum(rolls)
# simulated_avg = round(grand_total / 1000, 2)
# print(f"Simulated average total: {simulated_avg}")
# print("Theoretical average:     13.5")

# battle_quotes = [
#     "For glory and honor!",
#     "No retreat, no surrender!",
#     "Fortune favors the bold.",
#     "Hold the line!",
#     "Victory or death!",
# ]
# print()
# print(random.choice(battle_quotes))


# Problem 2 — Space Mission Calculator 🚀
# import math

# def distance(x1, y1, x2, y2):
#     return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

# def orbit_circumference(radius):
#     return round(2 * math.pi * radius, 2)

# def fuel_needed(mass, velocity):
#     energy = 0.5 * mass * velocity ** 2
#     return math.floor(energy * 100) / 100

# def bearing(x1, y1, x2, y2):
#     angle_radians = math.atan2(y2 - y1, x2 - x1)
#     angle_degrees = math.degrees(angle_radians)
#     return round(angle_degrees, 2)

# ship_pos = (0, 0)
# station_pos = (143, 892)
# orbit_radius = 6371
# ship_mass = 50000
# ship_velocity = 7800

# dist = distance(ship_pos[0], ship_pos[1], station_pos[0], station_pos[1])
# circumference = orbit_circumference(orbit_radius)
# fuel = fuel_needed(ship_mass, ship_velocity)
# log_velocity = round(math.log(ship_velocity, 10), 2)

# print("=== NAVIGATION REPORT ===")
# print(f"Distance to station:    {dist} units")
# print(f"Orbit circumference:    {circumference} km")
# print(f"Kinetic energy (fuel):  {fuel} J")
# print(f"Log10 of velocity:      {log_velocity}")

# ship_bearing = bearing(ship_pos[0], ship_pos[1], station_pos[0], station_pos[1])
# print(f"Bearing to station:     {ship_bearing} degrees")

# dist_ceiling = math.ceil(dist)
# dist_floor = math.floor(dist)
# print(f"Distance ceiling:       {dist_ceiling}")
# print(f"Distance floor:         {dist_floor}")

# Problem 3 — Animal Habitat Drawing 🐢
# import turtle
# import random

# def draw_sun(t, x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color("yellow")
#     t.begin_fill()
#     t.circle(40)
#     t.end_fill()

# def draw_tree(t, x, y, height=60):
#     # trunk
#     t.penup()
#     t.goto(x, y)
#     t.setheading(90)
#     t.pendown()
#     t.color("brown")
#     t.begin_fill()
#     for i in range(2):
#         t.forward(height)
#         t.right(90)
#         t.forward(15)
#         t.right(90)
#     t.end_fill()

#     # leaves
#     t.penup()
#     t.goto(x + 7, y + height)
#     t.pendown()
#     t.color("green")
#     t.begin_fill()
#     t.circle(30)
#     t.end_fill()

# t = turtle.Turtle()
# t.speed(0)
# screen = turtle.Screen()

# # grass strip
# t.penup()
# t.goto(-300, -150)
# t.pendown()
# t.color("green")
# t.begin_fill()
# for i in range(2):
#     t.forward(600)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
# t.end_fill()

# # sun
# draw_sun(t, 200, 200)

# # pond
# t.penup()
# t.goto(0, -130)
# t.pendown()
# t.color("blue")
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# # 3 fixed trees using a for loop
# tree_positions = [-250, -150, 150]
# for x_pos in tree_positions:
#     draw_tree(t, x_pos, -150)

# # Challenge: 10 random trees along the grass line, clamped so none draw off-screen
# for i in range(10):
#     random_x = random.randint(-280, 280)   # safe screen bounds
#     random_height = random.randint(40, 100)
#     draw_tree(t, random_x, -150, random_height)

# turtle.done()

# Problem 4 — Animal Guessing Game 🐾
# import random
# import math

# secret_number = random.randint(1, 100)
# secret_animal = "narwhal"

# guesses = []
# num_guesses = 0

# print("=== ANIMAL GUESSING GAME ===")
# print("A secret animal is waiting...")
# print()

# while True:
#     guess = int(input("Guess a number (1-100): "))
#     num_guesses += 1
#     guesses.append(guess)

#     if guess == secret_number:
#         print(f"CORRECT! The secret animal was: {secret_animal}")
#         print(f"You guessed it in {num_guesses} tries.")
#         break

#     distance = math.fabs(guess - secret_number)

#     if distance > 40:
#         print("Hint: ICE COLD")
#     elif distance > 20:
#         print("Hint: COLD")
#     elif distance > 10:
#         print("Hint: WARM")
#     else:
#         print("Hint: HOT!")
#     print()

# minimum_guesses = math.ceil(math.log2(100))
# print(f"Minimum possible guesses (optimal): {minimum_guesses}")

# # Challenge: track mean guess using math.fsum
# guess_sum = math.fsum(guesses)
# mean_guess = round(guess_sum / len(guesses), 2)
# print(f"Sum of all guesses: {guess_sum}")
# print(f"Mean guess: {mean_guess}")

# Problem 5 — Square Spiral 🌀
# import turtle

# laps = int(input("How many times around the square? "))
# color_mode = input("Color mode (type 'rainbow' or a color name): ")

# t = turtle.Turtle()
# t.speed(0)

# side_length = 10
# growth = 5
# total_sides = laps * 4

# rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# for i in range(total_sides):
#     if color_mode.lower() == "rainbow":
#         t.color(rainbow_colors[i % len(rainbow_colors)])
#     else:
#         t.color(color_mode)

#     t.forward(side_length)
#     t.right(90)
#     side_length += growth

# turtle.done()