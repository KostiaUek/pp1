
def f(x, y, d):
    for value in range(x, y + 1):
        value = str(value)
        if value.__contains__(d):
            return True

    return False


if __name__ == "__main__":
    print(f(10, 15, "14"))
