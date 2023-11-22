arr = [7, 3, 8, 5, 2]
even = []
odd = []
for e in arr:
    if e % 2 == 0:
        even.append(e)
    else:
        odd.append(e)

result = even + odd
print(result)
