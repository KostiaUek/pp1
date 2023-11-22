def f(detector):
    people_in_room = 0
    for char in detector:
        if char == "+":
            people_in_room += 1
        else:
            people_in_room -= 1

        if people_in_room >= 3:
            return True
    return people_in_room >= 3


print(f('+-++-++-+---'))
