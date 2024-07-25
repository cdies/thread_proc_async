import math
import time
from multiprocessing import Manager, Process
from typing import List

N_JOBS = 4
LOAD = 100_000_000


def summarizator(arr: List[int], i: int, summ: List[int]) -> None:
    begin = int(i * LOAD / N_JOBS)
    end = int((i + 1) * LOAD / N_JOBS)
    res = 0
    for k in range(begin, end):
        res += math.sqrt(arr[k])
    summ[i] = res

arr = list(range(LOAD))

start = time.time()

with Manager() as manager:
    summ = manager.list([0] * N_JOBS)
    processes = [None] * N_JOBS

    for i in range(N_JOBS):
        processes[i] = Process(target=summarizator, args=(arr, i, summ))
        processes[i].start()

    for i in range(N_JOBS):
        processes[i].join()

    res = sum(summ)


stop = time.time()

print(f"{N_JOBS} processes result: {int(res)}, time: {stop - start}")
