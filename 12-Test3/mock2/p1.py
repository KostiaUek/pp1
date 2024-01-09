

def f(n):
    numbers = list(str(n))
    max_number = int(numbers[0])
    min_number = int(numbers[0])
    for number in numbers:
        number = int(number)
        if number % 2 == 0:
            continue
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number

    count = max_number - min_number
    return count
if __name__ == "__main__":
    print(f(10852))
