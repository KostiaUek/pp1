def f(array):
    values = {}
    for element in array:
        if element in values.keys():
            values[element] += 1
        else:
            values[element] = 1

    for key, value in values.items():
        if value == 1:
            return key
    return None


if __name__ == "__main__":
    print(f([7, 7, 7, 7, 7, 5, 7]))
    print(f([3, 3, 3, 2, 3]))
