'''
    This is a simple program that checks if a character or letter is a vowel or consonant.

'''

letter = ""
while len(letter) < 1:
    letter = input("Enter a letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter =="u" or letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U":
    print(f"{letter} is a vowel!")
else:
    print(f"{letter} is a consonant!")
