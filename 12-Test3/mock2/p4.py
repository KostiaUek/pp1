def f(fnc, res):
    i = 0
    while i < len(res):
        if not fnc(res[i]):
            res.pop(i)
            continue
        i += 1
    return max(res) - min(res)


if __name__ == "__main__":
    res = [95, 90, 20, 50, 70]
    fnc1 = lambda x: x > 50
    print(f(fnc1, res))
