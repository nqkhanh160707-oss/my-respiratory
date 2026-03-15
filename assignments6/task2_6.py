Seasons = ["Spring", "Summer", "Autumn", "Winter"]

Month = int(input("Enter the month number (1-12): "))

if Month in [3, 4, 5]:
    print("The season is:", Seasons[0])
elif Month in [6, 7, 8]:
    print("The season is:", Seasons[1])
elif Month in [9, 10, 11]:
    print("The season is:", Seasons[2])
elif Month in [12, 1, 2]:
    print("The season is:", Seasons[3])
else :
    print("Invalid number. Cant find a season for this month.")