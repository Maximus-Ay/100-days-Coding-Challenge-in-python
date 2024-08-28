'''
    This is a simple python program that finds the sum of all the digits in a number
'''

def Sum_of_all_digits(number):
    sum = 0
    while number > 0:
        x = number % 10
        sum += x
        number //= 10
    return sum

print(Sum_of_all_digits(345))