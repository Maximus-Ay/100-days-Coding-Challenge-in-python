'''
    This is a simple python program that finds the number of elements in a python lists
'''
def count(list):
    count = 0
    for x in list:
        count+=1
    return count
    # Or just 
    # return len(list)

list = [1,2,3,4,5,6,7,2,5,3]
print(f"List: {list}")

print(f"The number of elements in the list is: {count(list)}")