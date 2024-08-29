'''
    This is a simple python program that does the power function using recursion
'''

def power_function(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power_function(base, exponent-1)

print(power_function(4,3))
