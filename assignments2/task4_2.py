def is_leap_year():
    """
    Asks for a year and determines if it's a leap year using divisibility rules.
    """
    try:
        year = int(input("Enter a year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter an integer year.")

# Example usage:
# is_leap_year()