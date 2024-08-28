'''
    This is a simple python program that finds the LCM of two numbers
'''
# We will use Euclidean Algorithm for this
def GCD(num1, num2):
    while num2!= 0:
        num1, num2 = num2, num1 % num2
    return num1

def LCM(num1, num2):
    return abs(num1 * num2) # gcd (a,b) 

print(LCM(3,4))