array = [[1, 3, 5], [8, 7, 2]]
print(array[0][0] + array[1][2])
print(array[0][1] + array[1][1])
sum_last_row = 0
for element in array[1]:
    sum_last_row += element
print(sum_last_row)
