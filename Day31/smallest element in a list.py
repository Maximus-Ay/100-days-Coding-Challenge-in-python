'''
    This is a simple program that finds the smallest element in a list

'''
list = []
size = int(input("Enter the size of the list: "))
print("Enter the elements of the list: ")
for element in range(size):
    userinput = int(input("Enter value: "))
    list.append(userinput)
list.sort()
print(f"The largest element in the list is {list[0]}")
