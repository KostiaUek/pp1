def words(text: str):
    return len(text.split())


def ordered(text: str):
    arr = text.split()
    arr.sort(key=len)
    return arr


def alphabetical(text: str):
    arr = sorted(text.split())
    return arr
