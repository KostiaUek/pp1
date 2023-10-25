personal_data = "Mr. John May, born on 1998-02-16"
print(f'Description: {personal_data}')
print(f'Name: {personal_data.split(" ")[1]}')
print(f'Surname: {personal_data.split(" ")[2].split(",")[0]}')
print(f'Initials: {personal_data.split(" ")[1][:1]}{personal_data.split(" ")[2].split(",")[0][:1]}')
print(f'Born: {personal_data.split(" ")[5]}')

