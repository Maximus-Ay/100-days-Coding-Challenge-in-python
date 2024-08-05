'''
    This is a simple program that finds the intersection between two lists
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

intersection = []
for element in elements1:
    if element in elements2:
        intersection.append(element)

print(f"The intersection between the two lists is: {intersection}")