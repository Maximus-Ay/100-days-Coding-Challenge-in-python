'''
    This program makes use of loops to print the prime numbers from 1 to 100
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
    

print("The prime numbers from 1 to 100 are: ")
for x in range(1, 101):
    if isPrime(x):
        print(x, end=" ")
    
