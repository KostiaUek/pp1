ean_13_number = input("Enter EAN_13 number: ")
if len(ean_13_number) == 13:
    print("Article number is correct")
    if ean_13_number.startswith("590"):
        print("Article manufactured in Poland")
