N = int(input("Enter N: "))
i = 2
n = 0
prime_numbers = []

while n < N:

    divisors = 0
    for x in range(1, i + 1):
        if not i % x:
            divisors += 1

    if divisors == 2:
        prime_numbers.append(i)
        n += 1

    i += 1

print("Prime numbers:", end=" ")

for element in prime_numbers:
    print(element, end=" ")

print()
