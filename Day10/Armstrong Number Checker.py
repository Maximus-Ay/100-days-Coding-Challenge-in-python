'''
    This is a simple program that determines if a number is armstrong or not.
    (An armstrong number is one in which the sum of the squares of the individual digits in 
    that number equals that exact number. e.g 371 = 3^3 + 7^3 + 1^3 = 371)
'''

def isArmstrong(number):
    total = 0
    x = number
    temp = number
    while x > 0:
        x = number % 10
        total += x **3
        number = int(number/10)

    if temp == total:
        return True
    else:
        return False


number = int(input("Enter a number: "))


if isArmstrong(number):
    print(f"{number} is an Armstrong number!")
else:
    print(f"{number} is not an Armstrong number!")
