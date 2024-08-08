'''
    This is a simple program to sort a list in ascending order,
    You can use built in function or just do it manually yourself
'''

def sorting_list_in_ascending_order(list):
    return sorted(list)

list = []
size = int(input("Enter the size of the list: "))
for x in range(size):
    userinput = int(input(f"Enter element {x+1}: "))
    list.append(userinput)
    
print(f"Before: {list}")
print(f"The sorted list is: {sorting_list_in_ascending_order(list)}")

