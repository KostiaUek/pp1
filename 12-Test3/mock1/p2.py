
def f(x, y, digit):
    count = 0
    for value in range(x, y + 1):
        value = str(value)
        values_list = list(value)

        for el in values_list:
            if el == str(digit):
                count += 1

    return count


if __name__ == "__main__":
    print(f(10, 15, 1))
