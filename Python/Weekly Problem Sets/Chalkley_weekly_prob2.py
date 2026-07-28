# Problem 1 — Pizza Party Planner 🍕

# def pizzas_needed(people, slices_per_person, slices_per_pizza, extra_percent=0):
#     buff_people = people + (people * extra_percent // 100)
#     total_slices = buff_people * slices_per_person
#     pizzas = (total_slices + slices_per_pizza - 1) // slices_per_pizza
#     return pizzas

# def leftover_slices(people, slices_per_person, slices_per_pizza):
#     total_slices = people * slices_per_person
#     pizzas = pizzas_needed(people, slices_per_person, slices_per_pizza)
#     leftover = pizzas * slices_per_pizza - total_slices
#     return leftover

# print("\n=== PIZZA PARTY PLANNER ===")
# people = int(input("How many guests?   "))
# slices_per_person = int(input("Slices per person: "))
# slices_per_pizza = int(input("Slices per pizza:  "))

# pizzas = pizzas_needed(people, slices_per_person, slices_per_pizza)
# pizzas_buff = pizzas_needed(people, slices_per_person, slices_per_pizza, extra_percent=15)
# leftover = leftover_slices(people, slices_per_person, slices_per_pizza)
# total_slices_bought = pizzas * slices_per_pizza

# print(f"\n=== PARTY SUMMARY ===\nGuests:           {people}\nPizzas to order:  {pizzas}\nTotal slices:     {total_slices_bought}\nLeftover slices:  {leftover}")
# print("\n=== BUFFER COMPARISON ===")
# print(f"Pizzas without buffer:  {pizzas}\nPizzas with 15% buffer: {pizzas_buff}")


# Problem 2 — Space Station Oxygen Monitor 🚀

# Write a function o2_status(level) that returns:
# def o2_status(level):
#     if level < 15:
#         return "CRITICAL"
#     elif level <= 18:
#         return "LOW"
#     elif level <= 23:
#         return "NORMAL"
#     else:
#         return "HIGH"
#
# Challenge
# def trend(readings):
#     last_three = readings[-3:]
#     if last_three[0] < last_three[1] < last_three[2]:
#         return "IMPROVING"
#     elif last_three[0] > last_three[1] > last_three[2]:
#         return "DECLINING"
#     else:
#         return "STABLE"
    
# # You are given the following hourly O2 readings (as a percentage):
# readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]
# counts = {"CRITICAL": 0, "LOW": 0, "NORMAL": 0, "HIGH": 0}

# # Use a for loop to process each reading, call your function, and print the hour and status.
# for time, level in enumerate(readings):
#     hour = time + 1
#     status = o2_status(level)
#     counts[status] += 1
#     print(f"Hour {hour:2}: {level:3}% - {status}")
#     if status == "CRITICAL":
#         print("*** ALERT: TAKE ACTION IMMEDIATELY ***")

# print("\n=== STATUS SUMMARY ===")
# print(f"NORMAL:    {counts['NORMAL']} hours\nLOW:       {counts['LOW']} hours")
# print(f"CRITICAL:  {counts['CRITICAL']} hours\nHIGH:      {counts['HIGH']} hours")
# print(f"Trend:     {trend(readings)}")

# Problem 3 — RPG Character Battle ⚔️

# import random
# # Write a function attack(defender_hp, damage) that subtracts damage from defender HP and returns the new HP (minimum 0).
# def attack(defender_hp, damage):
#     new_hp = defender_hp - damage
#     return max(new_hp, 0)
# # Write a function is_alive(hp) that returns True if HP > 0.
# def is_alive(hp):
#     return hp > 0
# # CHALLENGE function "critical hit"
# def critical_hit(damage):
#     if random.randint(1, 10) <= 2:
#         return damage * 2
#     else:
#         return damage
    
# # Starting Values:
# hero_hp = 100            # Hero starting health points
# monster_hp = 90          # Demon king starting health points
# round_num = 0            # round counter initialized
# # Use a while loop to simulate the battle. Each round:
# print("\n=== BATTLE START ===")
# # while is_alive(hero_hp) and is_alive(monster_hp):
# #     round_num += 1
# #     monster_hp = attack(monster_hp, 18)                 # The hero deals 18 damage to the monster.
# #     if is_alive(monster_hp):                            
# #         hero_hp = attack(hero_hp, 12)                   # If the monster is still alive, it deals 12 damage to the hero.
# # # Print the round number and both HP values after each exchange.
# #     print(f"Round {round_num}:  Hero HP: {hero_hp}   |  Monster HP: {monster_hp}")

# # CHALLENGE
# while is_alive(hero_hp) and is_alive(monster_hp):
#     round_num += 1
#     damage = critical_hit(18)
#     if damage > 18:
#         print("*** CRITICAL HIT! ***")
#     monster_hp = attack(monster_hp, damage)
#     if is_alive(monster_hp):
#         hero_hp = attack(hero_hp, 12)
#     print(f"Round {round_num}:  Hero HP: {hero_hp}   |  Monster HP: {monster_hp}")

# # Use conditionals after the loop to print who won.
# print()
# if is_alive(hero_hp):
#     print("HERO WINS! The monster has been defeated.")
# else:
#     print("MONSTER WINS! The hero has been defeated.")

# Problem 4 — Mission Clearance System 🪖

# def check_fitness(score):
#     return score >= 70

# def check_rank(rank):
#     return rank in ["Corporal", "Sergeant", "Lieutenant"]

# def check_service_years(years):
#     return years >= 2

# name = input("SOLDIER NAME: ")
# fitness_score = int(input("FITNESS SCORE: "))
# rank = input("RANK: ")
# years = int(input("YEARS OF SERVICE: "))

# checks = [
#     ("Fitness check", check_fitness, fitness_score),
#     ("Rank check", check_rank, rank),
#     ("Service check", check_service_years, years)
# ]

# all_passed = True

# print("\n=== MISSION CLEARANCE REPORT ===")
# print(f"Soldier: {name}\n")

# for check, check_function, value in checks:
#     result = check_function(value)

#     if result:
#         status = "PASS"
#     else:
#         status = "FAIL"

#     label_with_colon = check + ":"
#     print(f"  {label_with_colon:<15} {status}")

#     if result == False:
#         all_passed = False

# print()
# if all_passed:
#     print("FINAL STATUS: CLEARED FOR MISSION.")
# else:
#     print("FINAL STATUS: DENIED.")

    
# Problem 5 — Sports Leaderboard 🏆
athletes = [
    ("Jordan",  82, 15),
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14),
]

def goals_per_game(goals, games):
    if games == 0:
        return 0.0
    return round(goals / games, 2)

def mvp_candidate(gpg):
    return gpg >= 0.25

def grade(gpg):
    if gpg >= 0.30:
        return "A"
    elif gpg >= 0.25:
        return "B"
    elif gpg >= 0.18:
        return "C"
    elif gpg >= 0.10:
        return "D"
    else:
        return "F"

print("=== SEASON LEADERBOARD ===")
print("  Athlete       Games   Goals   GPG     MVP?  Grade")
print("  ------------------------------------------------")

grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for name, games, goals in athletes:
    gpg = goals_per_game(goals, games)
    is_mvp = mvp_candidate(gpg)
    letter = grade(gpg)
    grade_counts[letter] += 1

    if is_mvp:
        marker = "*"
    else:
        marker = ""

    row = "  " + name.ljust(14) + str(games).ljust(8) + str(goals).ljust(8) + str(gpg).ljust(8) + marker.ljust(6) + letter
    print(row)

top_name = athletes[0][0]
top_goals = athletes[0][2]

for name, games, goals in athletes:
    if goals > top_goals:
        top_name = name
        top_goals = goals
print(f"\nTop scorer: {top_name} ({top_goals} goals)")

print()
print("=== GRADE DISTRIBUTION ===")
for letter, count in grade_counts.items():
    print(f"\t  {letter}: {count}")