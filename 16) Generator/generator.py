
def  fun():
    x =  5
    for i in range(x):
        yield i
        

generator = fun()
#Use next(method) to access generator value
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
#Use for loop to access generator value
for i in generator:
    print(i)



# Generator Expression
gen_squares = (i * i for i in range(5))
print(gen_squares) # আউটপুট: <generator object <genexpr> at 0x...>
# Generator Expression থেকে মান অ্যাক্সেস করা
for num in gen_squares:
    print(num)

#Project Create using Generator .......................
def read_large_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip() # প্রতিটি লাইন রিটার্ন করুন

# একটি ডামি ফাইল তৈরি করা
with open("16) Generator\\large_data.txt", "w") as f:
    for i in range(100000):
        f.write(f"This is line {i}\n")

# Generator ব্যবহার করে লাইন প্রসেস করা
#For Loop Use করে
for line in read_large_file("16) Generator\\large_data.txt"):
    if "line 100" in line:
        print(line)
        break # প্রয়োজন হলে থামুন

# next() ফাংশন ব্যবহার করে
gen = read_large_file("16) Generator\\large_data.txt")

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
