def f(amount_to_pay):
    five_zl = amount_to_pay // 5
    two_zl = (amount_to_pay - int(five_zl) * 5) // 2
    one_zl = (amount_to_pay - int(five_zl) * 5 - int(two_zl) * 2)

    return five_zl + two_zl + one_zl
