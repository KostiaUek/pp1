amount = float(input('Amount: '))
print(f'Amount  : {amount.__round__(2)}')
print(f'VAT 23% :  {(amount * 0.23).__round__(2)}')

