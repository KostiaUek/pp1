a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))
p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
print(f'Triangle area: {area}')
print(f'Triangle circumference: {a + b + c}')
