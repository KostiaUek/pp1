h = 170
feet = h * 0.0328084
inches = round(float(f'0.{str(feet).split(".")[1]}') * 12, 0)
print(f'I am {h}cm tall, i.e. {int(feet)} feet and {int(inches)} inches')
