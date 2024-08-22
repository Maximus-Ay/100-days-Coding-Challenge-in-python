'''
    This is a simple python program that multiplies all numbers in a list
'''

def Multiply(mylist):
    product = 1
    for x in mylist:
        product *= x
    return product
list = [1,2,3,4]
print(list)
print(f"The product of all numbers in the list is {Multiply(list)}")