def f(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)

    return result


print(f'f(11) returns "{f(11)}"')
print(f'f(4) returns "{f(4)}"')
