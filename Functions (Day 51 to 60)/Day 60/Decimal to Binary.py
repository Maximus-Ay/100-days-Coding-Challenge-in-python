'''
    This is a simple program that converts from Decimal to Binary
'''

def Decimal_to_Binary(number):
    Binary_number = []
    temp = number
    while temp > 0:
        x = temp % 2
        Binary_number.append(x)
        temp //= 2
    
    for x in reversed(Binary_number):
        print(x,end='')

Decimal_to_Binary(25)