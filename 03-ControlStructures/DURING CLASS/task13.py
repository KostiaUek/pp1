number_1 = int(input('Enter number: '))
number_2 = int(input('Enter number: '))
if number_1 >= 0 or number_2 >= 0:
    print(f'At least one of entered numbers {number_1} and {number_2} is not negative')
else:
    print(f'Both of them are negative')
