import math

array = [2, 3, 7, 5, 4]
print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[::-1][0])
print(array[len(array) - 2])
print(array[0] + array[::-1][0])
print(array[math.floor(len(array) / 2)])

for element in array:
    print(element, end=" ")
