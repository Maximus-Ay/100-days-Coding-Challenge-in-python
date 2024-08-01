'''
    Prime Number checker program

'''

def isPrimeNumber(number):
    count = 0
    for x in range(1, number+1):
        if number % x == 0:
            count+=1
        
    if count == 2:
        return True
    else:
        return False


number = int(input("Enter a number: "))
if isPrimeNumber(number):
    print(f"{number} is a prime number!")
else:
    print(f"{number} is not a prime number!")