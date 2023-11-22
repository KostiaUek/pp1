number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))


def different(n1, n2, n3):
    return not (n1 == n2 == n3)


is_different = different(number_1, number_2, number_3)

print(f'Numbers {number_1}, {number_2} and {number_3} are {"different" if is_different else "not different"}')
