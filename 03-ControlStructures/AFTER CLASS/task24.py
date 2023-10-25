price_current = float(input('Current product price: '))
price_previous = float(input('Previous product price: '))
percentage = price_current / price_previous * 100
if percentage <= 90:
    print(f'Buy the product!! \nProduct price reduced by {int((100 - percentage).__round__(0))} %')
else:
    print('No good deals today :(')
