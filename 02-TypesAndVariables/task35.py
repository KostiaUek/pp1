from math import pi
circumference = float(input('Enter tree circumference: '))
print(f'Tree can be cut down: {(circumference / pi) >= 50}')
