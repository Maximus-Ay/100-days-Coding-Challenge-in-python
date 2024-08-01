'''
    So my objective is to print this triangle
            E D C B A
            D C B A
            C B A
            B A
            A


'''

rows = int(input("Enter the number of rows: "))
letters = [chr(num) for num in range(65, 91)]
for x in range(rows):
    for y in range(rows-x):
        print(letters[rows-y-x-1], end=" ")
    print()
