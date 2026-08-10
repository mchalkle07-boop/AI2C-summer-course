# You find the resource file, and you are somewhat surprised to see that the problem that needs to be solved deals with
# food.

# Here's some background information.  Martian colonists have simple joys — and pizza is one of them. Due to supply shortages,
# thin-atmosphere baking challenges, and incoming new colonists every meal must be optimized.

# You have been sent to Mars with three Automatrons that were designed specifically for making pizza.  The problem is
# that no one has taken the time to figure out which Automatron is most efficient (produces the most pizza with the least
# amount of dough).

# The first Automatron produces 2 circular pizzas (15 inch diameter) that require 20 units of dough.
# The second Automatron makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
# The third Automatron creates a square pizza with side length 18, that only requires 18 units of dough.

# As the Chief Engineer, you decide to write a Python Script to figure out which Automatron is most efficient.
# Once we avert total disaster and save all 1000 lives on board of the incoming shuttle,
# we will want to welcome them with some warm, Martian pizza after all.

# Write a Python Script to determine which of these are the best deal.  Use functions to calculate the areas of the pizzas.

# Once you have completed this, navigate to root directory to find Problem 3.

import math

# ======================
# Area functions
# ======================


def circle_area(diameter):
    """Area of a circle given its diameter."""
    radius = diameter / 2
    return math.pi * radius**2


def triangle_area(side):
    """Area of an equilateral triangle given a side length."""
    return (math.sqrt(3) / 4) * side**2


def square_area(side):
    """Area of a square given a side length."""
    return side**2


# ======================
# Automatron specs
# ======================

# Automatron 1: 2 circular pizzas, 15 inch diameter, 20 units of dough
automatron_1_area = 2 * circle_area(15)
automatron_1_dough = 20

# Automatron 2: 1 equilateral triangle pizza, side 20, 20 units of dough
automatron_2_area = triangle_area(20)
automatron_2_dough = 20

# Automatron 3: 1 square pizza, side 18, 18 units of dough
automatron_3_area = square_area(18)
automatron_3_dough = 18

# ======================
# Efficiency calculations
# ======================

efficiencies = {
    "Automatron 1 (2 circles, 15in diameter)": automatron_1_area / automatron_1_dough,
    "Automatron 2 (triangle, side 20)": automatron_2_area / automatron_2_dough,
    "Automatron 3 (square, side 18)": automatron_3_area / automatron_3_dough,
}

areas = {
    "Automatron 1 (2 circles, 15in diameter)": automatron_1_area,
    "Automatron 2 (triangle, side 20)": automatron_2_area,
    "Automatron 3 (square, side 18)": automatron_3_area,
}

# ======================
# Report results
# ======================

print("======Automatron Efficiency Report======\n")
for name in efficiencies:
    print(f"{name}")
    print(f"  Total pizza area: {areas[name]:.2f} sq in")
    print(f"  Efficiency: {efficiencies[name]:.2f} sq in per unit of dough\n")

best = max(efficiencies, key=efficiencies.get)
print(f"Most efficient Automatron: {best}")


def square_area(side):
    return side**2
