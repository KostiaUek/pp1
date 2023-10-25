name_1 = input('Enter first person name: ')
age_1 = int(input('Enter first person age: '))
name_2 = input('Enter second person name: ')
age_2 = int(input('Enter second person age: '))
if (age_1, age_2) >= (18, 18):
    print(f'Both {name_1} and {name_2} are adults')
else:
    if age_1 >= 18:
        print(f'{name_1} is an adult')
    if age_2 >= 18:
        print(f'{name_2} is an adult')
