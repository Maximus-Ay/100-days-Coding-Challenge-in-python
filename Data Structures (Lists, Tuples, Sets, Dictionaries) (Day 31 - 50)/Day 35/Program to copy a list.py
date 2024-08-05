'''
    This is a simple program that copies a list
'''
elements = []
size = int(input("Enter the size of the list: "))
for element in range(size):
    userinput = int(input(f"Enter element {element+1}: "))
    elements.append(userinput)
print(f"Original list: {elements}")
copy_of_list = elements
print(f"Copy of list: {copy_of_list}")

