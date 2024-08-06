'''
    This is a simple program that finds the union of two lists in python
'''
def union_of_two_lists(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    
    return list(list1.union(list2))

print("Getting input for the first list\n")
list1 = []
size = int(input("Enter the size of the first list: "))
for i in range(size):
    userinput = int(input(f"Enter the element {i+1}: "))
    list1.append(userinput)

print("Getting input for the second list\n")
list2 = []
size = int(input("Enter the size of the second list: "))
for i in range(size):
    userinput = int(input(f"Enter the element {i+1}: "))
    list2.append(userinput)

print(f"The union of the two lists, is: {union_of_two_lists(list1, list2)}")

