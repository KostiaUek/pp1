import sys

correct_pin = "0805"
for _ in range(3):
    pin = input('Enter the PIN code: ')
    if pin == correct_pin:
        print("Correct")
        sys.exit()
    else:
        print("Incorrect...")
print("Sorry, your payment card has been blocked.")
