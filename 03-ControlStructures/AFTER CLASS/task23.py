human_years = int(input('Enter dog age in human years: '))
dog_years = 0
if human_years - 2 > 0:
    dog_years = 21 + (human_years - 2) * 4
else:
    dog_years = human_years * 10.5

print(f'The dog`s age in dog’s years is {dog_years} years.')
