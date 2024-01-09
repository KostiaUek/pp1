import re


def f(vname: str):
    if len(vname) not in range(1, 6):
        return False

    if len(re.findall("^(_|[a-zA-Z])", vname)) == 0:
        return False

    for letter in list(vname):
        if not bool(re.search("^(_|[a-zA-Z]|[0-9])", letter)):
            return False
    return True


if __name__ == "__main__":
    print(f("_4x"))
