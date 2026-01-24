def check_zander_length():
    """
    Asks for the length of a zander in cm and checks against the 42 cm size limit.
    If below, instructs to release and reports the shortfall.
    """
    try:
        length = float(input("Enter the length of the zander in centimeters: "))
        if length >= 42:
            print("The zander meets the size limit. You can keep it.")
        else:
            shortfall = 42 - length
            print(f"The zander is {shortfall:.1f} cm below the size limit. Please release it back into the lake.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Example usage (in main program):
# check_zander_length()


def describe_cabin_class():
    """
    Asks for the cabin class and prints its description.
    Uses if-elif-else for classification; errors on invalid input.
    """
    cabin_class = input("Enter the cabin class (LUX, A, B, or C): ").strip().upper()  # Normalize for flexibility
    if cabin_class == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("A: above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("B: windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")

# Example usage:
# describe_cabin_class()


def check_hemoglobin():
    """
    Asks for biological sex and hemoglobin value, then classifies as low/normal/high.
    Uses nested if-else for sex-specific ranges.
    """
    sex = input("Enter biological sex (M for male, F for female): ").strip().upper()
    try:
        hemoglobin = float(input("Enter hemoglobin value (g/L): "))
        if sex == "F":
            if hemoglobin < 117:
                print("Hemoglobin value is low.")
            elif 117 <= hemoglobin <= 155:
                print("Hemoglobin value is normal.")
            else:
                print("Hemoglobin value is high.")
        elif sex == "M":
            if hemoglobin < 134:
                print("Hemoglobin value is low.")
            elif 134 <= hemoglobin <= 167:
                print("Hemoglobin value is normal.")
            else:
                print("Hemoglobin value is high.")
        else:
            print("Invalid sex input. Please enter M or F.")
    except ValueError:
        print("Invalid hemoglobin value. Please enter a number.")

# Example usage:
# check_hemoglobin()


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


import math

def calculate_unit_price(diameter_cm, price_usd):
    """
    Calculates unit price per square meter.
    Converts cm to m, computes area, then price per m².
    """
    radius_m = (diameter_cm / 2) / 100  # cm to m
    area_m2 = math.pi * (radius_m ** 2)
    if area_m2 == 0:
        return float('inf')  # Avoid division by zero
    return price_usd / area_m2

# Main program
try:
    print("Enter details for Pizza 1:")
    dia1 = float(input("Diameter (cm): "))
    price1 = float(input("Price (USD): "))
    unit1 = calculate_unit_price(dia1, price1)

    print("\nEnter details for Pizza 2:")
    dia2 = float(input("Diameter (cm): "))
    price2 = float(input("Price (USD): "))
    unit2 = calculate_unit_price(dia2, price2)

    if unit1 < unit2:
        print("Pizza 1 provides better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")
except ValueError:
    print("Invalid input. Please enter numeric values.")