def f(product_code):
    return (int(product_code[0]) + int(product_code[1]) + int(product_code[2])) % 7 == int(product_code[3])


print(f('2035'))