'''
    This is a simple python function that finds the sum of all elements in a list
'''
def MySum(mylist):
    sum = 0
    for x in mylist:
        sum += x
    return sum
# OR USING SIMPLE BUILT IN FUNCTION WE CAN JUST 
# return sum(mylist)

print(MySum([1,2,4,5,2,5,-8,45,-90,100]))