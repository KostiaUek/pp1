import re


def f(mnumbers):
    count = 0
    for number in mnumbers:
        if number.startswith("+") or number.startswith("-"):
            number = number[1:]
        if re.fullmatch("^[+\-]?[1-7a-dA-D]+$", number):
            count += 1
    return count


if __name__ == "__main__":
    print(f(["A05", "-3+1", "7ab8C", "+D1", "-22k"]))
