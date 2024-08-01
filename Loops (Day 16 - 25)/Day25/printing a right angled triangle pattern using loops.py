'''
    So in this program I will recreate the following pattern
                    A 
                    A B
                    A B C
                    A B C D
                    A B C D E
'''

rows = int(input("Enter the number of rows you want: "))
letters_of_alphabet = []
for letter in range(65, 91):
    letters_of_alphabet.append(chr(letter))

for x in range(rows):
    for y in range(x+1):
        print(letters_of_alphabet[y], end=" ")
    print()

