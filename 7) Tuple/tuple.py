vegetable = ("carrot", "broccoli", "spinach", "cabbage", "cauliflower")
for veg in vegetable:
    print(veg)
    
print(vegetable[0])  # Accessing the first element
print(vegetable[1:3])  # Slicing the tuple to get a sub-tuple

print((vegetable, "spinach"))  # Finding the index of "spinach"

print("SORTED: ", sorted(vegetable))  # Sorting the tuple (returns a list)
print(len(vegetable))  # Getting the length of the tuple
print("broccoli" in vegetable)  # Checking if "broccoli" is in the tuple
print("broccoli" not in vegetable)  # Checking if "broccoli" is not in the tuple    


num = (1, 2, 3, 4, 5)
print(num[0])  # Accessing the first element of the num tuple
print(num[1:3])  # Slicing the num tuple to get a sub-tuple
print(num + (6, 7))  # Concatenating another tuple to num
print(num * 2)  # Repeating the num tuple       
print(num.index(3))  # Finding the index of the number 3 in the num tuple
print(num.count(2))  # Counting occurrences of the number 2 in the num tuple

print(sum(num))  # Summing the elements of the num tuple
print(max(num))  # Finding the maximum value in the num tuple   
print(min(num))  # Finding the minimum value in the num tuple
# Tuple with mixed data types                                           
mixed_tuple = (1, "apple", 3.14, True)
print(mixed_tuple)  # Printing the mixed tuple  
# Tuple with a single element (note the comma)
single_element_tuple = (42,)  # Comma is necessary to define a single-element tuple 

print(single_element_tuple)  # Printing the single-element tuple
# Nested tuple example  
nested_tuple = (1, (2, 3), (4, 5, (6, 7)))
print(nested_tuple)  # Printing the nested tuple    7
# Tuple unpacking example



dis_tuple = (1, 2, 3, 4, 5)
# Unpacking the tuple into variables
a, b, c, d, e = dis_tuple
print(a)  # Output: 1
print(b)  # Output: 2               
print(c)  # Output: 3

nested_tuple_unpacking = (1, (2, 3), (4, 5, (6, 7)))
# Unpacking the nested tuple    
a, (b, c), (d, e, (f, g)) = nested_tuple_unpacking
print(a)  # Output: 1   
print(b)  # Output: 2
print(c)  # Output: 3


