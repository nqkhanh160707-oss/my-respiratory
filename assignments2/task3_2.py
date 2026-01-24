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