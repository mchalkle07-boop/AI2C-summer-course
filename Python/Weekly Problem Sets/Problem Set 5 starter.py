# Problem 1:

def recursive_squares(num: int) -> list[int]:
    if num == 0:
        return []
    return recursive_squares(num - 1) + [num * num]
    
def palindrome_checker(pal: str) -> str:
    pal = pal.lower()
    if len(pal) <= 1:
        return True
    if pal[0] != pal[-1]:
        return False
    return palindrome_checker(pal[1:-1])
    
def length(check: str):
    if check == []:
        return 0
    return 1 + length(check[1:])

def flatten(lst):
    if lst == []:
        return []
    first, rest = lst[0], lst[1:]
    if isinstance(first, list):
        return flatten(first) + flatten(rest)
    return [first] + flatten(rest)

# only runs when file is ran directly
if __name__ == "__main__":
    print(recursive_squares(5))               # [1, 4, 9, 16, 25]
    print(palindrome_checker("bacon"))         # False
    print(palindrome_checker("radar"))         # True
    print(palindrome_checker(""))              # True
    print(length([1, 2, 3]))                   # 3
    print(flatten([1, [2, 3], [4], 5]))        # [1, 2, 3, 4, 5]

# Problem 2

def fibonacci(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

def count_ways(stairs: int) -> int:
    if stairs == 0:
        return 1
    if stairs == 1:
        return 1
    return count_ways(stairs - 1) + (stairs -2)

def grid_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return grid_paths(m - 1, n) + grid_paths(m, n - 1)

def permutations(lst):
    if lst == []:
        return [[]]
    result = []
    for i in range(len(lst)):
        first = lst[i]
        rest = lst[:i] + lst[i + 1:]
        for p in permutations(rest):
            result.append([first] + p)
    return result

if __name__ == "__main__":

    print(fibonacci(0))                  # 0
    print(fibonacci(1))                  # 1
    print(fibonacci(6))                  # 8
    print(count_ways(3))                 # 3
    print(count_ways(4))                 # 5
    print(count_ways(0))                 # 1
    print(grid_paths(2, 2))              # 2
    print(grid_paths(3, 3))              # 6
    print(grid_paths(1, 1))              # 1
    print(permutations([1, 2]))          # [[1, 2], [2, 1]]
    print(permutations([1, 2, 3]))       # 6 permutations