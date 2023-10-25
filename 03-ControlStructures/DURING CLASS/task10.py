number = int(input("Enter a number: "))
number_absolute = number
if number < 0:
    number_absolute = -number
print(f'|{number}| = {abs(number_absolute)}')
