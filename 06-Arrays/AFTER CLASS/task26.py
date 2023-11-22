arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest = ""
for element in arr:
    if len(element) > len(longest):
        longest = element
print(longest)