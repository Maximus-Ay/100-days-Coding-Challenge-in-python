'''
    This is a python program that finds the sum of the squares of the first n natural numbers
'''

def Sum_of_Squares(n):
    sum = 0
    for x in range(1,n+1):
        sum = sum + pow(x, 2)
    
    return sum

n = int(input("Enter the value of n: "))
print(f"The sum of the first {n} natural numbers is: {Sum_of_Squares(n)}")
