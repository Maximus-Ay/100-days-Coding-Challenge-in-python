'''
    This is a simple python program that finds the symmetric difference between two lists
'''

def symmetric_difference(list1, list2):
    list1 = set(list1)
    list2 = set(list2)

    return list(list1.symmetric_difference(list2))

print("Getting imput for the first list\n")
list1 = []
size = int(input("Enter the size of the list: "))
for i in range(size):
    userinput = int(input(f"Enter element {i+1}"))
    list1.append(userinput)

print("Getting imput for the second list\n")
list2 = []
size = int(input("Enter the size of the list: "))
for i in range(size):
    userinput = int(input(f"Enter element {i+1}"))
    list2.append(userinput)

print(f"The symmetric difference between the two lists is: {symmetric_difference(list1, list2)}")
