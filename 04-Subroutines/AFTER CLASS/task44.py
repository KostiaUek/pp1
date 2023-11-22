def f(password):
    char_list = []
    for char in password:
        if char not in char_list:
            char_list.append(char)

    return len(char_list) >= 6


print(f(""))
