arr = [2, 3, 2, 5, 8, 1, 9, 8]
arr_dict = {}
unique = []
for element in arr:
    if element in arr_dict.keys():
        arr_dict[element] += 1
    else:
        arr_dict[element] = 1
for key, value in arr_dict.items():
    if value == 1:
        unique.append(key)

print(unique)
