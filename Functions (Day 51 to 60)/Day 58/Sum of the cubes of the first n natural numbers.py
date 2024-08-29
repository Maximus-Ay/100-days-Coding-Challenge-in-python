'''
    This is a python program that finds the sum of the cubes of the first n natural numbers
'''

def Sum_of_Cubes(n):
    sum = 0
    for x in range(1,n+1):
        sum = sum + pow(x, 3)
    
    return sum

n = int(input("Enter the value of n: "))
print(f"The sum of the cubes of the first {n} natural numbers is: {Sum_of_Cubes(n)}")