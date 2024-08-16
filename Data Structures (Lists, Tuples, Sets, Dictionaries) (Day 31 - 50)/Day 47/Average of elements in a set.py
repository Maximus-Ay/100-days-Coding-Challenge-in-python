'''
    This is a simple program that finds the average of all elements in a set
'''
mySet = {1,2,3,4,1}
print(mySet)
print(f"The sum of all elements in the set is: {sum(mySet)/len(mySet)}")
print("Note that it doesn't consider the elements two times, since its a set and sets do not accept duplicates")