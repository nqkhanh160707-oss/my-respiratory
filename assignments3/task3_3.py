numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    if numbers:
        print(f"Maximum: {max(numbers)}")
        print(f"Minimum: {min(numbers)}")
        
