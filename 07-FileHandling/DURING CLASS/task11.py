file = open('numbers.txt', 'r')
file_content = file.read().split()

result_sum = 0
result_string = "Numbers: "
for line in file_content:
    result_string += f'{line} '
    result_sum += int(line)

# close file
file.close()

print(result_string)
print(result_sum)
