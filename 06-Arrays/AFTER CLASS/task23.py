arr = [-15, 8, -31, 47, -2, 19]
minimal = arr[0]
maximum = arr[0]

for element in arr:
    if element < minimal:
        minimal = element
    if element > maximum:
        maximum = element

print(minimal)
print(maximum)
