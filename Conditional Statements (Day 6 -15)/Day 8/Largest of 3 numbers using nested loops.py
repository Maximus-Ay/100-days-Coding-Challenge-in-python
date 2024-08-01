'''
    This is a program to find the largest of 3 numbers using Nested loops

'''

firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
thirdNumber = float(input("Enter the third number: "))

if firstNumber > secondNumber:
    if firstNumber >= thirdNumber:
        print(f"{firstNumber} is the largest")
elif secondNumber > firstNumber:
    if secondNumber >= thirdNumber:
        print(f"{secondNumber} is the largest!")
elif thirdNumber > firstNumber:
    if thirdNumber >= secondNumber:
        print(f"{thirdNumber} is the largest!")
else:
    print(f"All the numbers are equal!")

