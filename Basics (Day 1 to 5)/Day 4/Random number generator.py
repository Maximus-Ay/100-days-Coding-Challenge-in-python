'''
    This is a basic program to generate random numbers from 1 to 100.
    We will make use of the random module in python to do that
'''
import random
print(f"Random numbers from 1 to 100 are:")
for i in range(100):
    print(random.randint(1,100), end=" ")
