
#🔸 উদাহরণ ১: List Spread → * ব্যবহার দুটি লিষ্ট একসাথে যুক্ত করা
list1 = [1, 2, 3]
list2 = [*list1, 4, 5]

print(list2) #➡️ Output: [1, 2, 3, 4, 5]

#🔸 উদাহরণ 2: Dictionary Unpacking → ** ** ব্যবহার দুটি ডিক্সক্কে  একসাথে যুক্ত করা
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = {**dict1, **dict2}

print(merged)   #➡️ Output: {'a': 1, 'b': 2}

#🔸 উদাহরণ ৩: Function Parameter → *args এবং **kwargs ব্যাবহার করে ফাংশনের মাঝে লিষ্ট বা টুপল এবং ডিকশনারী পাস করা আর্গুমেন্ট হিসেবে । 

def introduce(name, age, country):
    print(f"{name} is {age} years old from {country}.")

info_list = ["Tamim", 25, "Bangladesh"]
info_dict = {"name": "Tamim", "age": 25, "country": "Bangladesh"}

introduce(*info_list)
introduce(**info_dict)


#🔸 উদাহরণ ৪: Function Parameter → *args ব্যাবহার করে যে কোন ভ্যালু কে লিষ্ট বা টুপল  এ কনভার্ট করে  প্যারামিটার হিসেবে রিসিভ করে।, 
def employ_name(*name):
    n = name
    for i in n:
        print(i)

employ_name("Tamim", "Moniruzzaman")


def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3,8,9))  # Output: 6

#🔸 উদাহরণ ৫: Function Parameter → *kwargs ব্যাবহার করে যে কোন ভ্যালু কে ডিস্কশন্রী তে কনভার্ট প্যারামিটার হিসেবে  রিসিপ করা 
def employ_name(*name):
    n = name
    for i in n:
        print(i)

employ_name("Name : -->", "Moniruzzaman")




