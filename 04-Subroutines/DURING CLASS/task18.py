def numbers(n):
    numbers_string = []
    for i in range(1, n + 1):
        numbers_string.append(str(i))
    return " ".join(numbers_string)


print(f'Numbers <1, 15>: {numbers(15)}')
print(f'Numbers <1, 7>: {numbers(7)}')
