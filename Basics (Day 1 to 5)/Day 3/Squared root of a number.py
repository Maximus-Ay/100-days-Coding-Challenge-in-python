'''
    This is a simple program that get's input from the user and finds the squared root of that number.
'''

import math
# Getting input
number = float(input("Enter a number: "))
# Displaying output
decimal_places = int(input("How many decimal places: "))
print(f"The squared root of {number} = {math.sqrt(number):.{decimal_places}f}")

