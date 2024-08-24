'''
    This is a simple program that checks if a number is a prime number or not
'''

def Check_If_Prime(number):
    factors = 0
    for x in range(1, number+1):
        if number % x == 0:
            factors += 1
    
    if factors == 2:
        return True
    else:
        return False
    

print(Check_If_Prime(13))