'''
    This is a simple program that uses the notion or concept of while loops in python 
    to be able to print natural numbers from 1 to n.
'''
n = int(input("Enter the value of n: "))
print(f"The first {n} natural numbers are: ")
counter = 1
while counter <=n:
    print(counter, end=" ")
    counter+=1
