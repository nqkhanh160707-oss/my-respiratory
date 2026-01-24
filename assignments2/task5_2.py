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