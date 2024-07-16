'''
    This is a simple program that prints all the odd numbers from 1 to 100
'''
print("Odd numbers from 1 to 100 are: ")
counter = 1
while counter <=100:
    if counter % 2 == 1:
        print(counter, end=" ")
    counter += 1

