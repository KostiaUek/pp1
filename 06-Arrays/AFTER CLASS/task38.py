arr = [7, 3, 8, 5, 2]
value = int(input("Value: "))
result = 0
for e in arr:
    if e > value:
        result += 1

print(result)
