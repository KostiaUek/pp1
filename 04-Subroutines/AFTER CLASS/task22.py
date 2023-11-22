from mymonths import month


def get_month_name():
    number = int(input('Enter month number: '))
    return print(f'The name of the month {number} is {month(number)}')


get_month_name()
