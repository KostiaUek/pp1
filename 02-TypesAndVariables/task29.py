from random import choices

rolls = choices(range(1, 6), k=3)

print(f'First roll: {rolls[0]}')
print(f'Second roll: {rolls[1]}')
print(f'Third roll: {rolls[2]}')
print(f'Sum: {sum(rolls)}')
