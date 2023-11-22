arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]
result = []
for element in arr1:
    if element not in arr2:
        result.append(element)
print(result)
