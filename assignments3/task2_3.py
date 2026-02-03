while True:
    inch = float(input("Enter length in inches (negative to quit): "))
    if inch < 0:
        break
    cm = inch * 2.54
    print(f"{inch} inches is {cm} centimeters.")
    
