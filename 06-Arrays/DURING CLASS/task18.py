array = [[True, False], [True, True], [False, False]]
print(array)
for row in array:
    i = 0
    while i < len(row):
        row[i] = not row[i]
        i += 1

print(array)
