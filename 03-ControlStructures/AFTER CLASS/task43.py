fibonacci = [0, 1]

i = 2

while i < 21:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    i += 1

for f in fibonacci:
    print(f, end=" ")

print()
