'''
    This is a program that checks if a number entered by the user is a strong number
    A strong number is one in which the sum of the factorial of its digits is equal to the original 
    number itself. E.g 145 = 1! + 4! + 5!
'''
def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number * factorial(number-1)

def isStrongNum(number):
    temp = number
    Sum = 0
    while number > 0:
        x = number % 10
        Sum = Sum + factorial(x)
        number = number // 10
    
    if Sum == temp:
        return True
    else:
        return False


number = int(input("Enter a number: "))
if isStrongNum(number):
    print(f"{number} is a Strong number!")
else:
    print(f"{number} is not a strong number!")