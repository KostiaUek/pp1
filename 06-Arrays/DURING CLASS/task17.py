array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

i = 0
while i < len(array):
    array[i][i] = 1
    i += 1
for row in array:
    i = 0
    while i < len(row):
        if i != 2:
            print(row[i], end=" ")
        else:
            print(row[i])
        i += 1


