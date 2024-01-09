def f(uid):
    a = {}
    for uname in uid:
        if uname in a.keys():
            a[uname] += 1
        else:
            a[uname] = 1

    for val in a.values():
        if val > 1:
            return False

    return True


if __name__ == "__main__":
    print(f(["john5", "ann123", "john5", "xxx", "abc333", "a10"]))
