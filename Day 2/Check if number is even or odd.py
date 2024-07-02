'''
    This is a simple program that asks the user for some input and says if that number is even or odd.
'''
# Getting user input
number = int(input("Enter a number: "))
# Applying logic for even and odd number
if number%2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

