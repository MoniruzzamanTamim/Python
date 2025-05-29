 





set1 = {1, 2, 3, 4, 5}
set2 = {3,5,8,7,9}


set1.add(25)
# set2.remove(10)     # This will raise a KeyError if 10 is not present in set2
set1.discard(1)  # If the element is not present, it does nothing
set2.pop()  # Removes and returns an arbitrary element from the set
print("SET1: ", set1)  # Output: {1, 2, 3, 4, 5, 8, 7, 9, 25}
print("SET2:  ", set2)  # Output: {3, 5, 8, 7, 9} "


union= set1.union(set2)  # Returns a new set with all elements from both sets
print("Union: ", union)
set1.update(set2)  # Adds all elements from set2 to set1
print("Updated SET1: ", set1)  # Output: {1, 2, 3, 4, 5, 8, 7, 9, 25}
intersection = set1.intersection(set2)  # Returns a new set with elements common to both sets
print("Intersection: ", intersection)

difference = set1.difference(set2)  # Returns a new set with elements in set1 but not in set2
print("Difference: ", sorted(difference))  # Output: {1, 2, 4, 5, 25}
symmetric_difference = set1.symmetric_difference(set2)  # Returns a new set with elements in either set1 or set2 but not both
print("Symmetric Difference: ", symmetric_difference)  # Output: {1, 2, 4, 5, 7, 8, 9, 25}
disjoint = set1.isdisjoint(set2)  # Returns True if sets have no elements in common
print("Are the sets disjoint? ", disjoint)  # Output: False, since they share elements
are_equal = set1 == set2  # Checks if both sets are equal
print("Are the sets equal? ", are_equal)  # Output: False, since they have different elements
# Checking if a set is a subset or superset of another
is_subset = set1.issubset(set2)  # Returns True if set1 is a subset of set2
print("Is SET1 a subset of SET2? ", is_subset)  # Output: False
is_superset = set1.issuperset(set2)  # Returns True if set1 is a superset of set2   
print("Is SET1 a superset of SET2? ", is_superset)  # Output: True, since set1 contains all elements of set2
# Checking if a set is a proper subset or superset of another   
is_proper_subset = set1 < set2  # Returns True if set1 is a proper subset of set2
print("Is SET1 a proper subset of SET2? ", is_proper_subset)  # Output: False
is_proper_superset = set1 > set2  # Returns True if set1 is a proper superset of set2
print("Is SET1 a proper superset of SET2? ", is_proper_superset)  # Output: True, since set1 contains all elements of set2 and more
# Checking if a set is a subset or superset of another using issubset and issuperset methods    
print("Is SET1 a subset of SET2? ", set1.issubset(set2))  # Output: False
print("Is SET1 a superset of SET2? ", set1.issuperset(set2))  # Output: True    
# Checking if a set is a proper subset or superset of another using < and > operators
print("Is SET1 a proper subset of SET2? ", set1 < set2)  # Output: False


