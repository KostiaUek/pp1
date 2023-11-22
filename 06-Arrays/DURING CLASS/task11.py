months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']


def month(n):
    try:
        return months[n - 1]
    except:
        return "Wrong month number"


value = int(input("Enter month number: "))
print(f'Month name: {month(value)}')
