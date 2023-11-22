def f(number, even: bool):
    value = 0
    for element in list(str(number)):
        if int(element) % 2 != int(even):
            value += int(element)
    return value
