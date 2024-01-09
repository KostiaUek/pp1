def f(fnc, prods):
    result = ""
    for product in prods:
        prod_id = fnc(product)
        result += prod_id
        result += ","

    return result[:-1]


if __name__ == "__main__":
    prods = ["water", "cheese", "tomato"]
    fnc1 = lambda x: "id:" + x[:2]
    print(f(fnc1, prods))
