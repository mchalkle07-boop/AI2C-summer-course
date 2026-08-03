import requests
import json

# # Task 1:
# r = requests.get("https://jsonplaceholder.typicode.com/posts/1", auth=('user', 'pass'))
# r.status_code, r.reason


# # Task 2:
# r.headers["content-type"], r.elapsed
# # >>> ('application/json; charset=utf-8', datetime.timedelta(microseconds=78340))


# # Task 3:
# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)

# try:
#     data = response.json()
#    # r.json()["userId"] another way to get the info
#     print("userId:", data["userId"])
#     print("id:", data["id"])
#     print("title:", data["title"])
# except json.JSONDecodeError:
#     print("Error: could not parse JSON response")

# # Task 4
# r = requests.get("https://jsonplaceholder.typicode.com/comments", params={"postId=1": 1})
# data = r.json()

# print("Number of comments:", len(data))
# print("First comment email", data[0]["email"])

# Hands on 2:
# Task 1:
# >>> from requests.auth import HTTPBasicAuth
# >>> basic = HTTPBasicAuth('student', 'pass123')
# >>> requests.get('https://httpbin.org/basic-auth/student/pass123', auth=basic)
# <Response [200]>
# >>> requests.get('https://httpbin.org/basic-auth/student/pass123', auth=('student', 'pass123'))
# <Response [200]>
# print(response.reason, response.status_code)

# # Task 2:
# from requests.auth import HTTPBasicAuth

# # headers = {"Authorization": "Bearer" + "some api key"}
# # response = requests.get(f"{address}/get?api")

# class BearerAuth(HTTPBasicAuth):
#     """Attaches HTTP Bearer Authentication to the given Request object."""
#     def __init__(self, username):
#         # setup any auth-related data here
#         self.username = username

#     def __call__(self, r):
#         # modify and return the request
#         r.headers['Bearer'] = self.username
#         return r

# Task 4:

# print("Checking cookies")
# with requests.Session() as session:
#     response = session.get(f"{address}/cookies/set/course_token/python-lesson-10")
#     print(response.text)
#     response = session.get(f"{address}/cookies/set/second_token/my-second-cookie")
#     response = session.get(f"{address}/cookies")
#     print(response.request.headers)
# print()