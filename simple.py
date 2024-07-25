import math
import time
from typing import List

LOAD = 100_000_000


def summarizator(arr: List[int]) -> int:
    res = 0
    for n in arr:
        res += math.sqrt(n)
    return res

arr = list(range(LOAD))

start = time.time()
res = summarizator(arr)
stop = time.time()

print(f"Simple result: {int(res)}, time: {stop - start}")
