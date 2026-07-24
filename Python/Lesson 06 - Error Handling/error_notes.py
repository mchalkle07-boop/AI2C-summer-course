import random

# with open("numbers.txt", "w") as f:
    
#     for i in range(100):
#         some_numbers = random.randint(1, 1000)
#         f.write(str(some_numbers) + "\n")

# with open("numbers.txt", "r") as f:
#     lines = f.readlines()

# numbers = [int(line.strip()) for line in lines]

# m = max(numbers)
# mn = min(numbers)
# avg = sum(numbers) / len(numbers)

# print(f"Max number: {m}\nMinimum number: {mn}\nAverage of numbers: {avg}")


# Instructor example:
# with open("output.txt", "w") as f:
#     random_number = str(random.randint(1, 1000))
#     f.writelines(random_number + "\n")

# with open("output.txt", "r") as input_f:
#     lines = input_f.readlines()
#     lines_stripped = [int(line.strip())for line in lines]
# print(lines_stripped)

# min = 1000
# max = 0
# sum = 0
# count = 0

# for line in lines_stripped:
#     if line > max:
#         max = line
#     if line < min:
#         min = line
#     count += 1
#     sum += line

# average = sum / count
