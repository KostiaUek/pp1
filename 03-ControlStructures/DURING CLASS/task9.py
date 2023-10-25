total = int(input('How many tasks are there?: '))
done = int(input('How many tasks were completed?: '))

if done / total * 100 < 50:
    print("Test was not passed")
else:
    print("Test passed")
