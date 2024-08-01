'''
    This is a simple program that converts from kilometers to miles.
    Note that 1km = 0.62137119 miles.
    Hence x km = ?
'''
# getting user input in kilometers
kilo = float(input('Enter the distance in kilometers: '))
# Calculating distance in miles
miles = kilo * 0.62137119
# Displaying output
decimalPlaces = int(input("Enter the number of decimal places: "))
print(f"{kilo} km = {miles:.{decimalPlaces}f} miles")
