def f(number1, number2, number3):
    minimal = min(number1, number2, number3)
    maximal = max(number1, number2, number3)

    return maximal - minimal


print(f(2, 12, 9))
