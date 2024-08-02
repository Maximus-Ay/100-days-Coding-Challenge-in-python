'''
    This is a simple program to find the second smallest element in a list
'''
list = []
size = int(input("Enter the number of elements the list should contain: "))
for i in range(size):
    userinput = int(input("Enter an element: "))
    list.append(userinput)

list.sort()
print(f"The second largest element in the list is: {list[1]}")

