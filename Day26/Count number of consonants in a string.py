'''
    This is a simple program that counts the number of consonants in a String
    In English Language we have 5 vowels, which are a,e,i,o,u
    and so everyother except this is a consonant.
    and so while moving through the string we will check to see if we
    have any one of these vowels within we ignore it and count only those that are different from them

'''

string = input("Enter the string: ")
count_consonants = 0
for i in string:
    if not (i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'or i==' '):
        count_consonants += 1
print(f"The number of consonants in {string} is {count_consonants}")