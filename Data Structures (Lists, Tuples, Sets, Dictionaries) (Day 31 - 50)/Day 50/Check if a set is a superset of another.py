'''
    This is a simple python program that checks if a set is a superset of another
'''

set1 = {1,2,3,4,5,6,7}
set2 = {1,4,7}
print(f"Set1: {set1} and Set2: {set2}")
print(f"is Set 1 a superset of Set 2? {set1.issuperset(set2)}")