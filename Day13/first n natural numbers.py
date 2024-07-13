'''
    This is a program to print the first n natural numbers.
'''
print("This is a program to print the first n natural numbers: ")
n = int(input("Enter the value of n: "))
print(f"The first {n} natural numbers are: ")
for x in range(1,n+1):
    print(x, end=" ")
