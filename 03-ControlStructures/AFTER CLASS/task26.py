car_speed = float(input('Car speed (km/h): '))
speed_limit_min, speed_limit_max = 40, 140
if not speed_limit_min < car_speed < speed_limit_max:
    print("Warning: invalid car speed!!")
