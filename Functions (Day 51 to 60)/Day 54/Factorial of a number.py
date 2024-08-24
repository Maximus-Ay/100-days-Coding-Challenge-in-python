'''
    This is a simple program that finds the factorial of a number
'''

def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    
print(factorial(5))