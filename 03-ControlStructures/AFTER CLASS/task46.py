for i in range(1, 8):
    for x in range(0, 7):
        print(" " if (i + x * 7) in [8, 9] else "", i + x * 7, end=" ")
    print()
