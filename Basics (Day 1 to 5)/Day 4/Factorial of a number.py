'''
    This is a code to find the factorial of a number.
    There are two ways this can be done,
    1) Iteratively 
    2) Recursively

    But i will do it iteratively.
    The factorial of a number for example 5 is 5 x 4 x 3 x 2 x 1 = 120 and also note that the factorial of 0
    in arithmetic is considered to be 1. and the factorial of a negative number doesn't exist.

'''

factorial = 1
userInput = int(input("Enter the number: "))

for number in range(1, userInput + 1):
    factorial *= number

print(f"{userInput}! = {factorial}")

