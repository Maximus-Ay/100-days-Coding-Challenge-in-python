'''
    So this is a simple python program that, prints the right angled triangle pattern
    using numbers.
            1
            1 2
            1 2 3
            1 2 3 4
            1 2 3 4 5 
'''
rows = int(input("Enter the number of rows: "))
for x in range(rows):
    for y in range(x+1):
        print(y+1, end=" ")
    print()



