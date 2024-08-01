'''
    This is a program that finds the factorial of a number using recursion
    A recursion is a function that calls itself

'''

def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number * factorial(number-1)
    

number = int(input("Enter a number: "))
print(f"{number}! = {factorial(number)}")
