amount = int(input('Enter the amount in PLN: '))

five_zl = amount // 5
two_zl = (amount - int(five_zl) * 5) // 2
one_zl = (amount - int(five_zl) * 5 - int(two_zl) * 2)

print(f'The amount of PLN 18 in coins:\n5 zł – {five_zl}\n2 zł – {two_zl}\n1 zł – {one_zl}')
