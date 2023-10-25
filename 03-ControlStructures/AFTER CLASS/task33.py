decimal_number = int(input('Enter a decimal integer: '))

result = f'{decimal_number}(10) = '

binary_number = ""

while True:
    quotient = decimal_number // 2
    remainder = decimal_number % 2
    binary_number += str(remainder)

    if quotient == 0:
        break

    decimal_number = quotient

print(f'{result}{binary_number[::-1]}(2)')
