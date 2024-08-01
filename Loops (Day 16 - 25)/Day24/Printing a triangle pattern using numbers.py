'''
    So this is a simple python program that, prints the right angled triangle pattern
    using numbers.
            5 4 3 2 1
            4 3 2 1
            3 2 1
            2 1
            1
'''
rows = int(input("Enter the number of rows: "))
for x in range(rows):
    for y in range(rows-x):
        print(rows-y-x, end=" ")
    print()





