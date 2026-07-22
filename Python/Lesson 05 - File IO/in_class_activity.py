# import random

# # Ask user how many games they want to play 
# game_prompt = input("Lets play rock, paper scissors...\nPress ENTER to play...")

# # Force user input to only be odd numbers 1-9
# while True:
#     try:
#         games = int(input("How many games would you like to play (1, 3, 5, 7, 9): "))
#         if games in [1, 3, 5, 7, 9]:
#             break
#         print("Invalid choice. You must enter an odd number between 1 and 9.")
#     except ValueError:
#         print("Please enter a valid number.")

# game_count = 0

# # Loop through the exact number of games requested
# while game_count < games:
#     user_pick = input("\nPick rock, paper, or scissors: ").lower().strip()
    
#     if user_pick not in ["rock", "paper", "scissors"]:
#         print("Invalid choice! Please type rock, paper, or scissors.")
#         continue
        
#     computer_pick = random.choice(["rock", "paper", "scissors"])
#     print(f"Computer picked: {computer_pick}")

#     if user_pick == computer_pick: 
#         print("It's a tie!")
#     elif user_pick == "rock" and computer_pick == "scissors": 
#         print("You win! Rock beats scissors.")
#     elif user_pick == "paper" and computer_pick == "rock": 
#         print("You win! Paper beats rock.")
#     elif user_pick == "scissors" and computer_pick == "paper": 
#         print("You win! Scissors beats paper.")
#     else:
#         print(f"You lose! {computer_pick} beats {user_pick}.")
    
#     game_count += 1

# print("\nGame Over! Thanks for playing.")

# check = float(input("What is the amount of your check? "))
# tip_perc = float(input("What percent do you want to tip? "))

# def tip(total: float, percent: float) -> float:
#     return total * (percent / 100)

# total_tip = tip(check, tip_perc)
# total_tip2 = tip(100, 20)

# print(f"{total_tip:.2f}")
# print(f"{total_tip2:.2f}")


# def compound_int(p: float, r: float, t: int, n: int = 1) -> float: 
#     # Wrap n*t in parentheses so the entire product is treated as the exponent
#     return p * (1 + r/n) ** (n * t)

# print(compound_int(1000, .061, 10, 1)) # Output: 1807.72


# Manipulating Files:

