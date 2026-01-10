# task7.py
import random

# 3-digit code (0-9 for each digit)
print("3-digit combination:")
for _ in range(2):
    code3 = ""
    for _ in range(3):
        code3 += str(random.randint(0, 9))
    print(code3)

# 4-digit code (1-6 for each digit)
print("4-digit combination:")
for _ in range(2):
    code4 = ""
    for _ in range(4):
        code4 += str(random.randint(1, 6))
    print(code4)