'''
    This is a simple program that finds the length of a tuple.
    We can use the built-in functions or we can do it manually
'''
def lengthOfTuple(tuple):
    length = 0
    for x in tuple:
        length +=1
    return length

myTuple = (12,34,"Maximus",45,8.90,True)
print(f"Length of Tuple is: {lengthOfTuple(myTuple)}")
