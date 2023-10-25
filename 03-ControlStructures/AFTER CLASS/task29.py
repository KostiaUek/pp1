washing_product = "shoes"
rinse = True
spin = False
time = rinse * 15 + spin * 9
if washing_product == "jacket":
    time += 40
elif washing_product == "underwear":
    time += 70
elif washing_product == "shoes":
    time += 20

print(f'Total washing time: {time} minutes')
