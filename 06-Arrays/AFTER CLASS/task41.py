arr1 = [1, 2]
arr2 = [1, 2, 3]
result = True
for e in arr1:
    if e not in arr2:
        result = False
        break

print(result)
