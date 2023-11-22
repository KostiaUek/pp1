import random

arr = [1, 2, 3, 4, 5]


def rand_element(arr):
    random.shuffle(arr)
    return arr[0]


print(rand_element(arr))
