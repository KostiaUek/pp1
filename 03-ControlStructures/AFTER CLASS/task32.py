value1 = input('Are you interested in computer science? (Y/N): ') == "y"
value2 = input('Do you like playing computer games? (Y/N): ') == "y"
value3 = input('Do you have an Instagram account? (Y/N): ') == "y"

print(f'Interested in computer science: {"Yes" if value1 else "No"}')
print(f'Playing computer games: {"Yes" if value2 else "No"}')
print(f'Has an Instagram account: {"Yes" if value3 else "No"}')
