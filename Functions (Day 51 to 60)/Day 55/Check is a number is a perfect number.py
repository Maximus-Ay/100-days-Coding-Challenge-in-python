'''
    This is a simple python program that checks if a number is a perfect number
'''

def Check_If_Perfect_Number(number):
    sum_of_divisors = 0
    for x in range(1, number):
        if number % x == 0:
            sum_of_divisors += x
    if sum_of_divisors == number:
        return True
    else:
        return False

number = int(input("Enter the number to check if it is a palindrome: "))
print(Check_If_Perfect_Number(number))