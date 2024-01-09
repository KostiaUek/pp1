

def f(string: str):
    i = 0
    result = ""
    while i < len(string):
        end_string = "-"
        if len(string) - i == 1:
            end_string = ""
        result += string[:i] + string[i].upper() + string[i+1:] + end_string

        i += 1

    return result
if __name__ == "__main__":
    print(f("book"))
