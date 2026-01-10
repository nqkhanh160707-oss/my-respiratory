# task5.py
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

total_sum = num1 + num2 + num3
product = num1 * num2 * num3
average = total_sum / 3

print(f"The sum is: {total_sum}")
print(f"The product is: {product}")
print(f"The average is: {average}")
# Optional nicer formatting
print(f"The average is: {average:.2f}")