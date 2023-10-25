phone_number = input('Enter phone number: ')
print(f'Phone number: {"-".join(phone_number[::-1][i:i + 3] for i in range(0, len(phone_number), 3))[::-1]}')  # Inserts "-" every 3 chars from the end, much more flexible
print(f'Phone number: {phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}')
