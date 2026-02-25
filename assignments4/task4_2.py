number = int(input("Enter an integer: "))
if number <= 1:
    print("Not a prime number.")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime number.")
    else:
        print("Not a prime number.")