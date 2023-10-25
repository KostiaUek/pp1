number = int(input('Number of products purchased: '))
price = int(input('Product price: '))
total = 0
if number - 2 > 0:
    total = 2 * price + (number - 2) * price * 0.75
else:
    total = number * price
print(f'Amount to pay: {total.__round__(2)}')
