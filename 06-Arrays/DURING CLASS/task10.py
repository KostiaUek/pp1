import math

array = [1, 2, 3, 4, 5]
print(array)
array[0] = array[0] - 1
print(array)
array[-1] = array[-1] + 4
print(array)
array[math.floor(len(array) / 2)] = array[math.floor(len(array) / 2)] * 2
print(array)
