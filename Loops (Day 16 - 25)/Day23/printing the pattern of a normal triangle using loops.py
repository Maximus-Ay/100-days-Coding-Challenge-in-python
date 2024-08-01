'''
    This is a simple python progran that makes use of the notion of loops to be able to print
    the pattern of the following triangle:
                                 *
                                * *
                               * * * 
                              * * * * 
                             * * * * * 
'''

length = int(input("Enter the length of the triangle(rows) you wish to print: "))
for x in range(length):
    # Column
    # First for loop here is for the spaces
    for y in range(length-x-1):
        print(" ", end="")
    # This second for loop is to print the stars
    for j in range(x+1):
        print("*", end=" ")
    print()

