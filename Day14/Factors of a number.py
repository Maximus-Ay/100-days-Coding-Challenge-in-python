'''
    This is a simple program that helps us to be able to print all the factors of a number
'''

number = int(input("Enter the number: "))
print(f"Factors of {number} are: ")
for num in range(1, number+1):
    if number % num == 0:
        print(num, end=" ")



