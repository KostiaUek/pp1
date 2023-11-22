import random

arr = [random.randint(1, 1000) for _ in range(8)]
result = "|"
for e in arr:
    result += f' {str(e)}|'
print("-" * len(result))
print(result)
print("-" * len(result))
