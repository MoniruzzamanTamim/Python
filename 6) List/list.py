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