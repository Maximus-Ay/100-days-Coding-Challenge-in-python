'''
    This is a simple program that sums all the natural numbers between 1 and n
'''

n = int(input("Enter the value of n: "))
Sum = 0
for number in range(1, n+1):
    Sum+=number
print(f"The sum of all natural numbers from 1 to {n} is: {Sum}")

