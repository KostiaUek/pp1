def phone_keyboard():
    i = 6
    while i in [6, 3, 0]:
        j = 1
        while j < 4:
            print(f' {i + j}', end='')
            j += 1
        print()
        i -= 3


phone_keyboard()
