a = 4
b = 15

for i in range(1, a + 1):
    if i == 1 or i == a:
        print("*" * b)
    else:
        print("*" + " " * (b - 2) + "*")
