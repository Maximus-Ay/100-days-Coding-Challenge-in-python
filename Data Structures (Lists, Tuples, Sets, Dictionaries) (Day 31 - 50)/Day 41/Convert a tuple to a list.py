'''
    This is a simple program that turns a tuple into a list
'''

myTuple = (12,34,"Maximus",45,8.90,True)
print(f"Before: {myTuple}")
myTuple = list(myTuple)
print(f"After: {myTuple}")