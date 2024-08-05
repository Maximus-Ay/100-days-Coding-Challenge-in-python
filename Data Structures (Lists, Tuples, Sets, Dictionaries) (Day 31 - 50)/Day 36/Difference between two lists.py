'''
    This is a simple python program that finds the difference between two lists
'''

elements1 = []
size1 = int(input("Enter the size of the list: "))
for element in range(size1):
    userinput = int(input(f"Enter element {element+1}: "))
    elements1.append(userinput)

elements2 = []
size2 = int(input("Enter the size of the list: "))
for element in range(size2):
    userinput = int(input(f"Enter element {element+1}: "))
    elements2.append(userinput)

difference = []
for element in elements1:
    if element not in elements2:
        difference.append(element)

print(f"The difference between the two lists is: {difference}")


