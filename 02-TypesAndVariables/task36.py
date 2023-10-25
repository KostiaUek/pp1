b = float(input('Bank buys EUR: '))
s = float(input('Bank sells EUR: '))
print(f'Spread: {abs((b - s).__round__(4))}')
