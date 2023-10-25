from random import choice

roll = choice(range(1, 6))
print(f'Dice rolled: {roll}')
print(f'Special number: {roll == 1 or roll == 6}')
