def read_number():
    return int(input("Enter a number: "))


if __name__ == "__main__":
    a = read_number()
    b = read_number()
    print(f"{a} + {b} = {a + b}")
