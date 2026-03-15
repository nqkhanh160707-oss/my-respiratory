numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input == 'done':
        break
    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("5 biggest numbers:")
print(numbers[:5])