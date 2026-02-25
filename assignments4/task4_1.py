numbers = []
while True:
    user_input = input("Enter a number (press Enter to quit): ")
    if user_input == "":
        break
    number = int(user_input)
    numbers.append(number)
numbers.sort()
numbers.reverse()
print("Five greatest numbers:")
count = 0
for num in numbers:
    if count < 5:
        print(num)
        count += 1