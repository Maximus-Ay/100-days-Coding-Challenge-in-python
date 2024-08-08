'''
    This is a python program that sorts a list in descending order. 
    We are going to use a built in function to be able to accomplish this
'''
def sorting_list_in_descending_order(list):
    list = sorted(list)
    return list[::-1]
list = []
size = int(input("Enter the size of the list: "))
for i in range(size):
    userinput = int(input(f"Enter element {i+1}: "))
    list.append(userinput)

print(f"Before: {list}")
print(f"The list in descending order is: {sorting_list_in_descending_order(list)}")
