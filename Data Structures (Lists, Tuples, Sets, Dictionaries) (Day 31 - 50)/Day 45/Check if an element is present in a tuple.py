'''
    This is a simple program that checks if an element is found in a tuple
'''

myTuple = (1,2,3,5,6,8,9,10)
searchElement = int(input("Enter the search element: "))
if searchElement in myTuple:
    print(f"{searchElement} is in the tuple!")
    print(myTuple)
else:
    print(f"{searchElement} is not found within the list!")
    print(myTuple)