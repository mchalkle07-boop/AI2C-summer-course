# import random
# import math


# with open("signals.txt", "w") as s:
#     s.writelines()

# for i in range(1,100):
#     max_number = max(range(1,100))
#     if max_number >


# signals = []

# with open("pre_class.txt", "r") as in_f:
#     for line in in_f:
#         signal = int(line)
#         signals.append(signal)
# signals_sorted = sorted(signals, reverse=True)
# high_5 = signals_sorted[:5]
# coordinate = sum(high_5) / 10.0
# print(f"The coordinate is{coordinate}")

signals = []

with open("preclass_problem1_data.txt", "r") as f:
    for line in f:
        signal = int(line.strip())
        signals.append(signal)

signals_sorted = sorted(signals, reverse=True)
high_5 = signals_sorted[:5]
coordinate = sum(high_5) / 10.0
print(f"The coordinate is {coordinate}")


# # # Alternate method-
# with open("preclass_b.txt", "r") as infile:
#     print(f"The coordinate is {sum(sorted(int(x) for x in infile[-5:]) / 10)}")