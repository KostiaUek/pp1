x = 5
y = 2

location = ""
if (x, y) == (0, 0):
    location = "in the position (0,0)"
elif x and not y:
    location = "on the vertical axis"
elif y and not x:
    location = "on the horizontal axis"
elif (x, y) > (0, 0):
    location = "in the first quadrant of the coordinate system"
elif (x, y) < (0, 0):
    location = "in the third quadrant of the coordinate system"
elif x < 0 < y:
    location = "in the second quadrant of the coordinate system"
else:
    location = "in the forth quadrant of the coordinate system"

print(f'Point P{x, y} is {location}')
