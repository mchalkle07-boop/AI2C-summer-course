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
    print(recursive_squares(5))  # [1, 4, 9, 16, 25]
    print(palindrome_checker("bacon"))  # False
    print(palindrome_checker("radar"))  # True
    print(palindrome_checker(""))  # True
    print(length([1, 2, 3]))  # 3
    print(flatten([1, [2, 3], [4], 5]))  # [1, 2, 3, 4, 5]

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
    return count_ways(stairs - 1) + (stairs - 2)


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
        rest = lst[:i] + lst[i + 1 :]
        for p in permutations(rest):
            result.append([first] + p)
    return result


if __name__ == "__main__":

    print(fibonacci(0))  # 0
    print(fibonacci(1))  # 1
    print(fibonacci(6))  # 8
    print(count_ways(3))  # 3
    print(count_ways(4))  # 5
    print(count_ways(0))  # 1
    print(grid_paths(2, 2))  # 2
    print(grid_paths(3, 3))  # 6
    print(grid_paths(1, 1))  # 1
    print(permutations([1, 2]))  # [[1, 2], [2, 1]]
    print(permutations([1, 2, 3]))  # 6 permutations

# Problem 3

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id: int) -> dict:
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return {}


def create_user(name: str, job: str) -> dict:
    response = requests.post(f"{BASE_URL}/users", json={"name": name, "job": job})
    if response.status_code == 201:
        return response.json()
    return {}


def update_user(user_id: int, name: str, job: str) -> dict:
    response = requests.put(
        f"{BASE_URL}/users/{user_id}", json={"name": name, "job": job}
    )
    if response.status_code == 200:
        return response.json()
    return {}


def delete_user(user_id: int) -> bool:
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    return response.status_code == 200


# --- Challenge ---


def get_users_page(page: int) -> list[dict]:
    response = requests.get(f"https://reqres.in/api/users?page={page}")
    if response.status_code == 200:
        return response.json().get("data", [])
    return []


def partial_update_user(user_id: int, updates: dict) -> dict:
    response = requests.patch(f"https://reqres.in/api/users/{user_id}", json=updates)
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    # GET a user
    user = get_user(2)
    print(f"User: {user['name']} ({user['email']})")

    # POST to create a user
    new_user = create_user("John Doe", "Developer")
    print(f"Created user with ID: {new_user['id']}")

    # PUT to update a user
    updated = update_user(2, "Jane Smith", "Manager")
    print(f"Updated: {updated}")

    # DELETE a user
    success = delete_user(2)
    print(f"Deleted: {success}")

    # Challenge: get a page of users
    page_users = get_users_page(1)
    print(f"Page 1 users: {len(page_users)}")

    # Challenge: partially update a user
    patched = partial_update_user(2, {"job": "Senior Developer"})
    print(f"Patched: {patched}")

# Problem 4

import os

# import requests
# -imported above

# --- TMDB (query-param API key) ---


def search_movie(api_key: str, query: str) -> dict:
    response = requests.get(
        "https://api.themoviedb.org/3/search/movie",
        params={"api_key": api_key, "query": query},
    )
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]
    return {}


# --- GitHub (Bearer token in header) ---


def _github_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def get_github_user(token: str, username: str) -> dict:
    response = requests.get(
        f"https://api.github.com/users/{username}", headers=_github_headers(token)
    )
    if response.status_code == 200:
        return response.json()
    return {}


def create_gist(token: str, description: str, filename: str, content: str) -> str:
    response = requests.post(
        "https://api.github.com/gists",
        headers=_github_headers(token),
        json={
            "description": description,
            "public": True,
            "files": {filename: {"content": content}},
        },
    )
    if response.status_code == 201:
        return response.json().get("id", "")
    return ""


def delete_gist(token: str, gist_id: str) -> bool:
    response = requests.delete(
        f"https://api.github.com/gists/{gist_id}", headers=_github_headers(token)
    )
    return response.status_code == 204


if __name__ == "__main__":
    TMDB_API_KEY = "paste_your_key_here"
    GITHUB_TOKEN = "paste_your_token_here"

    # Fail fast with a clear message instead of a confusing KeyError later
    if not TMDB_API_KEY:
        raise RuntimeError(
            "TMDB_API_KEY is not set. Set it in your terminal before running, e.g.\n"
            '  PowerShell: $env:TMDB_API_KEY = "your_key_here"\n'
            "  cmd:        set TMDB_API_KEY=your_key_here"
        )
    if not GITHUB_TOKEN:
        raise RuntimeError(
            "GITHUB_TOKEN is not set. Set it in your terminal before running, e.g.\n"
            '  PowerShell: $env:GITHUB_TOKEN = "your_token_here"\n'
            "  cmd:        set GITHUB_TOKEN=your_token_here"
        )

    # Search for a movie
    movie = search_movie(TMDB_API_KEY, "The Matrix")
    if movie:
        print(f"Title: {movie['title']}, Year: {movie['release_date'][:4]}")
    else:
        print(
            "search_movie returned no result — check your TMDB_API_KEY is valid and active."
        )

    # Get GitHub user info
    user = get_github_user(GITHUB_TOKEN, "octocat")
    if user:
        print(f"{user['name']} has {user['public_repos']} public repos")
    else:
        print("get_github_user returned no result — check your GITHUB_TOKEN is valid.")

    # Create and delete a gist
    gist_id = create_gist(GITHUB_TOKEN, "My test gist", "test.txt", "Hello World!")
    if gist_id:
        print(f"Created gist: https://gist.github.com/{gist_id}")
        success = delete_gist(GITHUB_TOKEN, gist_id)
        print(f"Deleted: {success}")
    else:
        print("create_gist failed — check your GITHUB_TOKEN has the 'gist' scope.")
