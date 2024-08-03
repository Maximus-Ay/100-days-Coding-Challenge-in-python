'''
    This is a simple program that removes all the duplicates in a list
'''

elements = []
size = int(input("Enter the size of the list: "))
for element in range(size):
    userinput = int(input(f"Enter element {element+1}: "))
    elements.append(userinput)
print(f"Before: {elements}")
elements = set(elements)
print(f"The list without duplicates is: {list(elements)}")
