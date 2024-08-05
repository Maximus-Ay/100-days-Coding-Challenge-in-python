'''
    This is a program that finds the common elements between two lists

'''

elements1 = []
size1 = int(input("Enter the size of the list: "))
for element in range(size1):
    userinput = int(input(f"Enter element {elements1+1}: "))
    elements1.append(userinput)

elements2 = []
size2 = int(input("Enter the size of the list: "))
for element in range(size2):
    userinput = int(input(f"Enter element {elements2+1}: "))
    elements2.append(userinput)
common_elements = []
for i in range(size1):
    for j in range(size2):
        if elements1[i] == elements2[j]:
            common_elements.append(j)
            