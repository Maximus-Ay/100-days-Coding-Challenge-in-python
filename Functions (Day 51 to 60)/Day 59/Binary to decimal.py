'''
    This is a python program that convets from Binary to Decimal
'''

def Binary_to_Decimal(number):
    exp = 0
    Sum = 0
    while number > 0:
        x = number % 10
        Sum = Sum + (x * pow(2, exp))
        exp += 1
        number //= 10
    return Sum

print(Binary_to_Decimal(1101))