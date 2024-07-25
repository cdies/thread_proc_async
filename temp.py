# LOAD = 100
# N_JOBS = 3

# for i in range(N_JOBS):
#     begin = int(i * LOAD / N_JOBS)
#     end = int((i + 1) * LOAD / N_JOBS)
#     print(begin, end)

arr = [1,2,3]

def test(arr):
    arr[0] = 10

test(arr)

print(arr)