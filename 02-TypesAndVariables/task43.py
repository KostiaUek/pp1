word = input('Name: ')
print(f'{"".join(str(char) + "(" + str(ord(char)) + ")" + " " for char in word)}')
