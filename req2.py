import requests

payload = {"page": 2, "count": 25}
r = requests.get("http://httpbin.org/get", params=payload)

print(r.content)
# b'{\n  "args": {\n    "count": "25", \n    "page": "2"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.24.0", \n    "X-Amzn-Trace-Id": "Root=1-611d5ad2-5809e7506e9cb3d221d7beee"\n  }, \n  "origin": "103.254.56.152", \n  "url": "http://httpbin.org/get?page=2&count=25"\n}\n'
print(r.url)
# http://httpbin.org/get?page=2&count=25

payload2 = {"username": "Jenny", "password":"testing"}
r1 = requests.post("http://httpbin.org/post", data=payload2)
print(r1.text)
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "password": "testing",
#     "username": "Jenny"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "31",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.24.0",
#     "X-Amzn-Trace-Id": "Root=1-611d5bba-6dd7b3211207b5ae41a47e03"
#   },
#   "json": null,
#   "origin": "103.254.56.152",
#   "url": "http://httpbin.org/post"
# }
r_dict = r1.json()
print(r_dict["form"])
# {'password': 'testing', 'username': 'Jenny'}