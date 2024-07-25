import time

import requests


def get_request() -> dict:
    response = requests.get("http://localhost:23555")
    return response.json()

def first():
    data = get_request()
    print(1, data)

def second():
    data = get_request()
    print(2, data)


def main():
    first()
    second()


start = time.time()
main()
stop = time.time()

print(f"Request without async/await, time: {stop - start}")
