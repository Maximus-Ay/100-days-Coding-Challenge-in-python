'''
    This is a simple program that makes use of the concept of loops to be able to find the sum of
    all prime numbers from 1 to 100
'''

def isPrime(number):
    count = 0
    for num in range(1, number+1):
        if number % num == 0:
            count += 1
        
    if count == 2:
        return True
    else:
        return False
    
# Main program
total = 0
for value in range(1, 101):
    if isPrime(value):
        total += value
    
print(f"The sum of prime numbers from 1 to 100 is: {total}")
