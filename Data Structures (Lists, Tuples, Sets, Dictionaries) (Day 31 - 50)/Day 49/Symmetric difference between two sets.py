'''
    This is a simple program that finds the symmetric difference between two sets
'''
set1 = {1,2,3,4,5,6,7}
set2 = {1,4,5,9,10,22}
print(f"Set 1 = {set1} and Set 2 = {set2}")
difference = (set1.symmetric_difference(set2))
print(f"The union of the two sets are: {difference}")
