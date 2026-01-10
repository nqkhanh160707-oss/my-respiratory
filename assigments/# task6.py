# task6.py
# Conversions (as given):
# 1 talent = 20 pounds
# 1 pound = 32 lots
# 1 lot = 13.3 grams

talents = int(input("Enter talents: "))
pounds = int(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Convert everything to grams first
grams_from_talents = talents * 20 * 32 * 13.3
grams_from_pounds = pounds * 32 * 13.3
grams_from_lots = lots * 13.3

total_grams = grams_from_talents + grams_from_pounds + grams_from_lots

kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

print(f"The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.1f} grams.")
# Note: the example output has 545.95, so we keep one decimal