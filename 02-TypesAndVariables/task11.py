fathers_income = float(input('Enter father’s income: '))
mothers_income = float(input('Enter mother’s income: '))
number_of_ppl = int(input('Enter number of people in family: '))
total_income = fathers_income + mothers_income
print(f'Total income: {total_income}')
print(f'Income per person: {total_income / number_of_ppl}')
