import time
from threading import Thread
import requests

N_JOBS = 10
LOAD = 5


def get_request(begin: int, end: int):
    for i in range(begin, end):
        response = requests.get("http://localhost:23555")
        print(i, response.json())


start = time.time()

threads = [None] * N_JOBS
for i in range(N_JOBS):
    begin = int(i * LOAD / N_JOBS)
    end = int((i + 1) * LOAD / N_JOBS)
    threads[i] = Thread(target=get_request, args=(begin, end))
    threads[i].start()

for i in range(N_JOBS):
    threads[i].join()

stop = time.time()

print(f"Request {N_JOBS} threads, time: {stop - start}")
