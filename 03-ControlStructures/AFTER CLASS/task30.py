time_24 = input('Enter time (24-hour format): ')
hours = int(time_24.split(":")[0])
minutes = int(time_24.split(":")[1])
time_12 = ""
if hours > 12:
    time_12 = f'{hours - 12}:{minutes}pm'
elif hours == 12:
    time_12 = f'{time_24}pm'
elif hours == 0:
    time_12 = f'12:{minutes}am'
else:
    time_12 = f'{time_24}am'
print(f'Time in 12-hour format: {time_12}')
