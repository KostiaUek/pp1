def f(n):
    i = 0
    number = 0
    while i <= n:
        while True:
            number += 1
            if number in [2, 3, 5] or number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
                break
        i += 1

    return number


print(f(5))
