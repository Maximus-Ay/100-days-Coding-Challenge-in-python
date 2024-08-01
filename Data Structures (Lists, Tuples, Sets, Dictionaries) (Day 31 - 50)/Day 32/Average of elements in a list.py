'''
    This is a simple program that finds the average of the elements in a list
'''
list = []
size = int(input("Enter the number of elements you want in the list: "))
for element in range(size):
    userinput = int(input(f"Enter element {element + 1}: "))
    list.append(userinput)
print(f"The average of the elements in the list is {sum(list)/size:.2f}")
