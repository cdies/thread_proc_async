import math
import time
from threading import Lock, Thread
from typing import List

N_JOBS = 4
LOAD = 100_000_000


def summarizator(arr: List[int], i: int, summ: List[int], lock: Lock) -> None:
    begin = int(i * LOAD / N_JOBS)
    end = int((i + 1) * LOAD / N_JOBS)
    res = 0
    for k in range(begin, end):
        res += math.sqrt(arr[k])
    with lock:
        summ[i] = res

arr = list(range(LOAD))

start = time.time()

summ = [0] * N_JOBS
threads = [None] * N_JOBS
lock = Lock()

for i in range(N_JOBS):
    threads[i] = Thread(target=summarizator, args=(arr, i, summ, lock))
    threads[i].start()

for i in range(N_JOBS):
    threads[i].join()

res = sum(summ)


stop = time.time()

print(f"Threads result: {int(res)}, time: {stop - start}")
