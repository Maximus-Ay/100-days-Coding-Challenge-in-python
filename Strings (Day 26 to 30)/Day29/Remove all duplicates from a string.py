'''
    This is a simple program that removes all duplicates from a string
'''
string = input("Enter the string: ")
list = []
for x in string:
    list.append(x)
list = set(list)
for x in list:
    print(x, end="")
    
