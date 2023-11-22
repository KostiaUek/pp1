def f(n):
    i = 3
    a = 0
    b = 1

    current = 0
    while i <= n:
        current = a + b
        a = b
        b = current
        i += 1

    return current


print(f(9))
