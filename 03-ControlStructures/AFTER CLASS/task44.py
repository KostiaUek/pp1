numbers = []
while True:
    number = int(input("Enter number: "))

    if not number:
        print(f'RESULT: Quantity={len(numbers)}, Sum={sum(numbers)}, Mean={sum(numbers) / len(numbers)}')
        break

    numbers.append(number)
