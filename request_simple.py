import time

import requests


LOAD = 5


def get_request(begin: int, end: int):
    for i in range(begin, end):
        response = requests.get("http://localhost:23555")
        print(i, response.json())

start = time.time()
get_request(0, LOAD)
stop = time.time()

print(f"Request simple, time: {stop - start}")
