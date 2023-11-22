from myrange import is_inrange

x = 2
y = 15

number = int(input("A number: "))

print(f'Number {number} in the range <{x},{y}>: {"yes" if is_inrange(x, y, number) else "no"}')
