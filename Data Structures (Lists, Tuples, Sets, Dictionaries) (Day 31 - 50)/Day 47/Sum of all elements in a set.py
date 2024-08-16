'''
    This is a simple progtam that finds the sum of all elements in a set
'''

mySet = {1,2,3,4,1}
print(mySet)
print(f"The sum of all elements in the set is: {sum(mySet)}")
# Note: The answer will be 10, because it doesn't accept duplicates. Hence, only the first
# occurence of each element will be considered.