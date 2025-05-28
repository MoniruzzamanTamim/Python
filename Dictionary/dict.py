


student = {
    "name": "John Doe", 
    "age": 20,
    "courses": ["Math", "Science"],
    "is_active": True,
}

# 1==>  ==>
# Accessing values Using keys Name
print(student)
student["courses"].append("History")  # Adding a new course
print("#1 ==> ==>  Accessing values Using keys Name")
print(student["name"])  # Output: John Doe
print(student["courses"])  # Output: ['Math', 'Science', 'History']
print(student["age"]) # Output: 20
print(student["is_active"])  # Output: True


# 2==> ==>
print(" # 2 ==> ==> Using get method to access values")
# Using get method to access values
print(student.get("name"))  # Output: 20
# Using get method to access values
print(student.get("Name"))  # Output: None (no error, returns None if key doesn't exist)
# Using get method to access values
print(student.get("Name", "Show TAMIM"))  # Output: Show TAMIM (no error, returns Show TAMIM if key doesn't exist)


# 3==> ==> Access Values Using KEY,VALUES,ITEM METHOD
print("# 3==> ==> Access Values Using KEY,VALUES,ITEM METHOD")
print("Access Values Using key() Method", student.keys())
print("Access Values Using Values() Method", student.values())
print("Access Values Using Items() Method", student.items())


# 4==> ==> Access All Data Using For Loop 
print("# 4==> ==> Access All Data Using For Loop ")
for key in student.keys():
    print("Key:", key)  # Output: Key: name, Key: age, Key: courses, Key: is_active, Key: grade, Key: location
for value in student.values():
    print("Value:", value)  # Output: Value: TAMIM, Value: 21, Value: ['Math', 'Science', 'History'], Value: True, Value: A, Value: Elephent Load   
for key, value in student.items():          
    print("Key:", key, "Value:", value)  # Output: Key: name Value: TAMIM, Key: age Value: 21, Key: courses Value: ['Math', 'Science', 'History'], Key: is_active Value: True, Key: grade Value: A, Key: location Value: Elephent Load



# 5==> ==> Adding / Updating Items 
print("5==> ==> Adding / Updating Items ")
student["name"] = "TAMIM"  # Updating the name
print("After Updating key-Vallue:" , student["name"])  # Output: TAMIM
student.update({"age":25})  # Updating the age
print("After Updating key-Vallue:" , student["age"])  # Output: 21
student["grade"] = "A"  # Adding a new key-value pair
print("After Adding key-Vallue:" , student["grade"])  # Output: A
student.update({"location": "Elephent Load"})  # Add a new key-value pair
print("After Adding new key-Vallue:" , student["location"])  # Output: Elephent Load



#6 ==> ==>  Remove Or Delete Items
print("#6 ==> ==> Remove Or Delete Items")
# Using pop method to remove a key-value pair
removed_course = student.pop("courses")  # Removes the 'courses' key and returns its value      
print("Removed courses:", removed_course)  # Output: Removed courses: ['Math', 'Science', 'History']
# Using del statement to remove a key-value pair    
del student["is_active"]  # Removes the 'is_active' key
print("After deleting 'is_active':", student)  # Output: {'name': 'TAMIM', 'age': 21, 'grade': 'A', 'location': 'Elephent Load'}    


# 7==> ==> Copying a dictionary    
print("#7==> ==> Remove Or Delete Items")      
student_copy = student.copy()  # Creates a shallow copy of the dictionary
print("Copied Dictionary:", student_copy)  # Output: Copied Dictionary: {'name': 'TAMIM', 'age': 21, 'grade': 'A', 'location': 'Elephent Load'}

#8 ==> ==>  Clearing a dictionary
print(" #8 ==> ==> Clear Dictionary")
student.clear()  # Removes all key-value pairs from the dictionary
print("After clearing the dictionary:", student)  # Output: After clearing the dictionary: {}

# Creating a new dictionary     
new_student = {
    "name": "Alice",
    "age": 22,
    "courses": ["English", "History"],
    "is_active": False,
}

#9 ==> ==>  Merging dictionaries
print("#9 ==> ==> Merge Dictionary")
merged_student = {**new_student, **student_copy}  # Merges new_student and student_copy 
print("Merged Dictionary:", merged_student)  # Output: Merged Dictionary: {'name': 'Alice', 'age': 22, 'courses': ['English', 'History'], 'is_active': False, 'grade': 'A', 'location': 'Elephent Load'}



# Nested dictionaries   
nested_student = {
    "name": "Bob",
    "details": {
        "age": 23,
        "courses": ["Physics", "Chemistry"],
        "is_active": True,
    },
}   

#10 ==> ==> Accessing nested dictionary values
print("#10 ==> ==> Accessing nested dictionary values")         
print("Nested Name:", nested_student["name"])  # Output: Bob
print("Nested Age:", nested_student["details"]["age"])  # Output: 23
print("Nested Access Using GEt Method", nested_student["details"].get("is_active"))  # Output: True
print("Nested Courses:", nested_student["details"]["courses"])  # Output: ['Physics', 'Chemistry']  
print("Nested Key Access Using key method", "Key:" , nested_student["details"].keys())  # Output: dict_keys(['age', 'courses', 'is_active'])
print("Nested Value Access Using value method", "value:",nested_student["details"].values())  # Output: dict_values([23, ['Physics', 'Chemistry'], True]) D 
print("Nested Key & Value Access Using Items() method", "ITEMS :",nested_student["details"].items())  # Output: dict_values([23, ['Physics', 'Chemistry'], True]) D 

#11 ==> ==> Iterating through nested dictionary for loop

print("#11 ==> ==> Iterating through nested dictionary")
for key,value in nested_student["details"].items():
    print("Nested Key:", key, "&", "Nested Value:", value)  # Output: Nested Key: age Nested Value: 23, Nested Key: courses Nested Value: ['Physics', 'Chemistry'], Nested Key: is_active Nested Value: True


# #12 ==> ==> Dictionary Comprehension
# print("#12 ==> ==> Dictionary Comprehension")   
# # Creating a new dictionary using dictionary comprehension
# squared_numbers = {x: x**2 for x in range(1, 6)}  # Creates a dictionary with numbers as keys and their squares as values
# print("Squared Numbers Dictionary:", squared_numbers)  # Output: Squared Numbers Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}





nested_student["details"]["grade"] = "B"  # Adding a new key-value pair to the nested dictionary
print("After Adding new key-Vallue to nested dictionary:", nested_student["details"].get("grade"))  # Output: B
nested_student["details"].update({"location": "City Park"})  # Adding another key-value pair to the nested dictionary
print("After Adding new key-Vallue to nested dictionary:", nested_student["details"].get("location"))  # Output: City Park
nested_student["details"].update({"grade": "B+"})  # Updating the grade in the nested dictionary
print("After Updating key-Vallue in nested dictionary:", nested_student["details"].get("grade"))  # Output: B+


# More Nested Dictionary Operation

print("Courses in nested dictionary:", nested_student["details"].get("courses"))  # Output: ['Physics', 'Chemistry']
nested_student["details"]["courses"].append("Biology")  # Adding a new course to the nested dictionary
print("After Adding new course in nested dictionary:", nested_student["details"].get("courses"))  # Output: ['Physics', 'Chemistry', 'Biology']
# Removing a course from the nested dictionary  
nested_student["details"]["courses"].remove("Chemistry")  # Removes 'Chemistry' from the courses list
print("After Removing course in nested dictionary:", nested_student["details"].get("courses"))  # Output: ['Physics', 'Biology']
# Accessing nested dictionary values using a for loop   


