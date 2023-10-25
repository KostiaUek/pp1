from random import choice

roll = choice(range(1, 6))
guess = int(input('What number did I get?: '))
print(guess == roll)
