import mymath
import mykeyboard

number_user = mykeyboard.read_number()
number_algorithm = mymath.generate_number()
print(f'Computer number: {number_algorithm}')
print("You won the game!!" if number_user == number_algorithm else "YOu lost")

