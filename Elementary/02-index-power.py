def index_power(arr, N):
    if N < len(arr):
        return arr[N] ** N
    else:
        return  -1
print(index_power([1, 2, 3, 4], 2) == 9)
print(index_power([1, 3, 10, 100], 3) == 1000000)
print(index_power([0, 1], 0) == 1)


def index_power_best(arr, n):
    try:
        return arr[n] ** n
    except IndexError:
        return -1