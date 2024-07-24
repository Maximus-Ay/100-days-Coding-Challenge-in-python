'''
    This is a simple python program that makes use of loops, to print a simple 
    pattern below:
        * 
        * *
        * * *
        * * * *
        * * * * * 
'''

length = int(input("Enter the length of the triangle(dimensions or height): "))
for x in range(length):
    for y in range(x+1):
        print("*", end=" ")
    print()

