'''
    Finding the index of an element in a list
'''

list = []
size = int(input("Enter the size of the list: "))
for x in range(size):
    userinput = int(input(f"Enter the element {x+1}: "))
    list.append(userinput)

search_element = int(input("Enter the search element: "))
print(f"Index of element is: {list.index(search_element)}")


