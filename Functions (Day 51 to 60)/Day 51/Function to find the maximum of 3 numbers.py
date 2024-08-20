'''
    This is a python function to find the maximum of three numbers
'''

def Max(num1, num2, num3):
    return max(num1,num2,num3)
# OR WE COULD CODE IT MANUALLY WITHOUT USING A BUILT-IN FUNCTIOn
#   if num1 > num2 and num1 > num3:
#       return num1
#   elif num2 > num1 and num2 > num3:
#       return num2
#   elif num3 > num1 and num3 > num2:
#       return num3
#   else:
#       return "All a numbers are equal"
print(Max(2,2,2))