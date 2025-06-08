#📘 উদাহরণ ও ব্যাখ্যা ▶️ সাধারণ লুপ:
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n * n)
print(squares)#আউটপুট: [1, 4, 9, 16, 25]

#▶️ একই কাজ List Comprehension দিয়ে:
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares) #ফলাফল একদম একই: [1, 4, 9, 16, 25]

#✅ Filter (if condition সহ): ▶️ সাধারণভাবে:
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
#▶️ List Comprehension দিয়ে:
even = [n for n in numbers if n % 2 == 0] #আউটপুট: [2, 4]

#✅ কিছু বাস্তব উদাহরণ:
#🔹 1. স্ট্রিং থেকে ভাওয়েল বাদ দিয়ে ক্যারেক্টার লিস্ট বানাও:
text = "Bangladesh"
no_vowel = [c for c in text if c.lower() not in "aeiou"]
print(no_vowel)  # ['B', 'n', 'g', 'l', 'd', 's', 'h']
#🔹 2. List থেকে সব সংখ্যা ডাবল করে নতুন লিস্ট:
nums = [10, 20, 30]
double = [n * 2 for n in nums]

#🔹 3. Dictionary থেকে keys লিস্টে নাও:
info = {"name": "Tamim", "age": 25, "country": "Bangladesh"}
keys = [k for k in info]
# বা: keys = list(info.keys())

#✅ Nested List Comprehension (2D list)
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4]

