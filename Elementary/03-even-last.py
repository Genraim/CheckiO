def checkio(array):
    sum = 0
    for i in range(len(array)):
        if i % 2 == 0:
            sum += array[i]
        print(i, sum)
    if len(array) != 0:
        sum *= array[-1]
    return sum
#print(checkio([0, 1, 2, 3, 4, 5]) == 30)
#print(checkio([1, 3, 5]) == 30)
print(checkio([1, 3, 5]))
#print(checkio([6]) == 36)
#print(checkio([]) == 0)


def checkio_best(array):
    if len(array) == 0:
        return 0
    return sum(array[0::2]) * array[-1]