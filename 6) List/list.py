names = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan",
    "Fiona", "George", "Hannah", "Ian", "Jasmine",
    "Kevin", "Luna", "Michael", "Nina", "Oscar",
    "Paula", "Quinn", "Rachel", "Sam", "Tina"
]

#print Array Data using Index

#প্রথম থেকে ভ্যালু দেখা 
print("প্রথম থেকে ভ্যালু দেখা ")
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[19])

#শেষ থেকে  ভ্যালু দেখা 
print("শেষ থেকে  ভ্যালু দেখা")
print(names[-1])
print(names[-2])
print(names[-3])
print(names[-19])
print(names[-20])





#Print Vallue using index slicing

print(names[0:11])
print(names[11:20])
print(names[-5:])


names.reverse()
print(names)


#Print Vallue using For Loop 
names = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan",
    "Fiona", "George", "Hannah", "Ian", "Jasmine",
    "Kevin", "Luna", "Michael", "Nina", "Oscar",
    "Paula", "Quinn", "Rachel", "Sam", "Tina"
]


print("Using FOR LOOP....................................")
for name in names:
    print(name)

for nam in names:
    if nam.lower()=="hannah":
        print("This is For Loop & IF Statement")
        for nem in nam:
            print(nem)
        if nem =="n":
                print("very Nested")
             


#List Method 
fruits = ["apple", "banana", "cherry"]
#1️⃣ append(x) → লিস্টের শেষে উপাদান যোগ করা
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
#2️⃣ insert(i, x) → নির্দিষ্ট স্থানে উপাদান ঢোকানো
fruits.insert(1, "mango")
print(fruits)  # ['apple', 'mango', 'banana', 'cherry', 'orange']
#3️⃣ pop() → শেষ উপাদান সরিয়ে ফেলা
fruits.pop()
print(fruits)  # ['apple', 'mango', 'banana', 'cherry']
#4️⃣ pop(0) → শুরু থেকে উপাদান সরানো বা নির্দিষ্ট ইন্ডেক্স থেকে ভ্যালু সরানো
fruits.pop(0)
print(fruits)  # ['mango', 'banana', 'cherry']
#5️⃣ insert(0, x) → শুরুতে উপাদান যোগ করা বা নির্দিষ্ট ইন্ডেক্স এ ভ্যালু যোগ করা 
fruits.insert(0, "pineapple")
print(fruits)   #['pineapple', 'mango', 'banana', 'cherry']
#6️⃣ remove(x) → নির্দিষ্ট মান মুছে ফেলা
fruits.remove("banana")
print(fruits)   #['pineapple', 'mango', 'cherry']
#7️⃣ index(x) → উপাদানের অবস্থান বের করা
print(fruits.index("mango"))    #1
#8️⃣ x in list → উপাদান আছে কিনা যাচাই
print("cherry" in fruits)  # True
print("grape" in fruits)   # False
#9️⃣ reverse() → উল্টে দেওয়া
fruits.reverse()
print(fruits)  # ['cherry', 'mango', 'pineapple']
#🔟 sort() → সাজানো (Alphabetically / Numerically)
fruits.sort()
print(fruits)  # ['cherry', 'mango', 'pineapple']
#1️⃣1️⃣ copy() বা [:] → কপি তৈরি // লিষ্ট এর হুবহু একটা কপি তৈরি করা
new_fruits = fruits.copy()
# অথবা: new_fruits = fruits[:]
print(new_fruits)  # ['cherry', 'mango', 'pineapple']
#1️⃣2️⃣ clear() → সব উপাদান মুছে ফেলা

fruits.clear()
print(fruits)  # []
#1️⃣3️⃣ extend() → আরেকটি লিস্ট জোড়া দেওয়া
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # [1, 2, 3, 4]
#1️⃣4️⃣ count(x) → উপাদান কয়বার আছে

numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  # 3


# List unpacking example  
list_example = [1, 2, 3, 4, 5]
# Unpacking the list into variables 
a, b, c, d, e = list_example
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3   
print(d)  # Output: 4
print(e)  # Output: 5


# List with mixed data types
mixed_list = [1, "apple", 3.14, True]
print(mixed_list)  # Printing the mixed list
# List with a single element (note the comma)
single_element_list = [42]  # Comma is not necessary for a single-element list  
print(single_element_list)  # Printing the single-element list


# Nested list example   
nested_list = [1, [2, 3], [4, 5, [6, 7]]]
print(nested_list)  # Printing the nested list  
# List with a list of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]    
print(list_of_lists)  # Printing the list of lists
# List with a list of dictionaries                  
list_of_dicts = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
print(list_of_dicts)  # Printing the list of dictionaries   
# List with a list of tuples
list_of_tuples = [(1, 2), (3, 4), (5, 6)]   
print(list_of_tuples)  # Printing the list of tuples
# List with a list of sets
list_of_sets = [{1, 2}, {3, 4}, {5, 6}] 
print(list_of_sets)  # Printing the list of sets 
# List with a list of functions


# Nested List unpacking example
nested_list = [1, [2, 3], [4, 5, [6, 7]]]
a, (b, c), (d, e, (f, g)) = nested_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4
print(e)  # Output: 5
print(f)  # Output: 6
print(g)  # Output: 7
