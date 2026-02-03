import random
target = random.randint(1, 100)
while True:
        guess = int(input("Guess the number (1-100): "))
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print("Congratulations! You guessed it!")
            break