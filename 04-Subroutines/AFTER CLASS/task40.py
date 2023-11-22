def f(number):
    digits_dict = {}

    for digit in str(number):
        if str(digit) in digits_dict:
            digits_dict[str(digit)] += 1
        else:
            digits_dict[str(digit)] = 1

    result = 0

    for digit, count in digits_dict.items():
        if count > 1:
            result += int(digit) * count

    return result


print(f(513553007))
