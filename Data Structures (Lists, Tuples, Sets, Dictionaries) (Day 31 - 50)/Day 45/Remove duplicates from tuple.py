'''
    This is a simple python program that removes every duplicate from a tuple.
'''

myTuple = (1,2,3,4,2,5,6,1,2,7,9,2,3,4,8,9)
print(f"Before: {myTuple}")
myTuple = tuple(set(myTuple))
print(f"After: {myTuple}")
