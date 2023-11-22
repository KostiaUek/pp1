def f(name):
    result = ""
    words = name.split(" ")
    for word in words:
        result += word[:1]
    return result


if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
