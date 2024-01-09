file = open('countries.txt', 'r')
file_content = file.read().split()

# display text file, line by line
counter = 0
for line in file_content:
    counter += 1
    print(f"{counter}. {line}")

# close file
file.close()
