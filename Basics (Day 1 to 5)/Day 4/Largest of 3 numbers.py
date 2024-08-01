'''
    This is a simple program to find the largest of 3 numbers, There are two ways to do this:
    1- Using the function max, 
    2- Going through the logic of it all.
'''

# Method 1 : Using the max() method, that python provides.
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
thirdNumber = float(input("Enter the third number: "))

print(f"The largest number here is: {max(firstNumber, secondNumber, thirdNumber)}")

# Method 2: Using the normal logic
'''
if firstNumber > secondNumber and firstNumber > thirdNumber:
    print(f"{firstNumber} is the largest!")
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print(f"{secondNumber} is the largest!")
elif thirdNumber > firstNumber and thirdNumber > secondNumber:
    print(f"{thirdNumber} is the Largest!")
else:
    print('All the numbers are equal')

'''

# I could still use a list to do this, then sort the list and return the first number.
numbers = []
for number in range(3):
    userinput = int(input(f"Enter a number No {number+1}: "))
    numbers.append(userinput)
numbers.sort()
print(f"The greatest number is {numbers[len(numbers)- 1]}")




