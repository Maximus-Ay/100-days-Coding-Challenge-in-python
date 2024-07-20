'''
    This is simple program that finds the sum of numbers in a given range

'''

low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the higher bound of the range: "))

total = 0

for number in range(low, high+1):
    total+=number

print(f"Sum of numbers between {low} and {high} is {total}")
