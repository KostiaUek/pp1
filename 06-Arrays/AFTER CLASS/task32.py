def occurs(number, array):
    return number in array


arr = [15, 38, 7, 23, 14]

entered = int(input("Input a number: "))

print(occurs(entered, arr))
