'''
    This is a program that verifies if a number is either positive, negative or zero.
    A positive number is a number greater than 0
    A negative number is a number lower than zero.


'''

number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive!")
elif number < 0:
    print(f"{number} is negative!")
else:
    print(f"{number} is zero")

