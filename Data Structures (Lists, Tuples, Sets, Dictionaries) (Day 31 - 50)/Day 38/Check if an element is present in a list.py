'''
    This is a simple python program that checks to see if an element is present in a list
'''

list = [1,2,3,20,35,45,-89, 132]

element = int(input("Enter the search element: "))

if element in list:
    print(element, "is found in list")
    print("list:", list)
else:
    print(element, "is not found in list")
    print("List:", list)



