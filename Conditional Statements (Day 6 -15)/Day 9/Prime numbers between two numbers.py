'''
    This is a simple program that prints prime numbers between a given range given by user
'''

def isPrime(Number):
    count = 0
    for x in range(1,Number+1):
        if Number % x == 0:
            count+=1

    if count == 2:
        return True
    else:
        return False


low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the higher bound of the range: "))

for prime in range(low, high+1):
    if isPrime(prime):
        print(prime, end=" ")

