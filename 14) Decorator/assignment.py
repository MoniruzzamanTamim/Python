class Village:
    def __init__(self):
        pass
    @staticmethod
    def repeat(n):
        def decorator(fun):
            def inner_dec(*agrs, **kwagrs):
                for _ in range(n):
                    fun(*agrs, **kwagrs)
            return inner_dec
        return decorator
    @staticmethod
    @repeat(3)
    def person(name):
        print(f"Hello, {name}")


Shahinur =Village()

Shahinur.person("shahinur")


#🔹 Q1: Logging Decorator
from functools  import wraps
import time 
def log_function(func):
    @wraps(func)
    def inner_decorator(*args, **kwargs):
        start_time = time.time()
        name = func.__name__
        value = func(*args, **kwargs)
        time.sleep(2)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Start {name} Function \nFunction Start  Time {start_time}\nYour Argument {args} & {kwargs} \nFinal Result {value} \nFunction End Time {end_time} \nTotal Execution Time {total_time} ")
    return inner_decorator


@log_function
def Sum_number(a,b):
    sum = a+b
    print( "Sum Number",sum)

Sum_number(10,15)



print('\nrequire_admin...............................................................')

def require_admin(func):
    @wraps(func)
    def inner_decorator(*args, **kwargs):
        user_type = input("Please Type Your UserName: ")
        password = input("Please type Your Password: ")
        
        if user_type =="admin" and password == "admin":
            print("Access Grunted.....")
            func(*args, **kwargs)
        else:
            print("Please type Valid User Name Password")
    return inner_decorator

@require_admin
def bank_info():
    print("Total Amount = 1000000tk")

bank_info()

#🔹 Q3: Count Function Calls

def count_function_call(func):
    @wraps(func)
    def inner_decorator():
        inner_decorator.count_call +=1
        print(f"Function {func.__name__} is Called {inner_decorator.count_call} Time")
        func()
    inner_decorator.count_call = 0
    return inner_decorator

@count_function_call
def person():
    print("Hello")

person()
person()
person()
person()


#🔹 Q4: Decorator Chaining (Multiple Decorators)

def bold(func):
    @wraps(func)
    def inner_decorator(*a,**b):
        result = func(*a,**b)
        return f"<b>{result}<b>"
    return inner_decorator

def italic(func):
    @wraps(func)
    def inner_decorator(*a,**b):
        result = func(*a,**b)
        return f"<i>{result}<i>"
    return inner_decorator

@bold
@italic
def greet():
    return "Hello"

print(greet())



#একটি ডেকোরেটর তৈরি করো @retry(n) যা কোনো ফাংশনে exception উঠলে সর্বোচ্চ n বার পর্যন্ত পুনরায় চেষ্টা করবে।

import random
def retry(n):
    def decorator(func):
        @wraps(func)
        def inner_decorator(*a, **b):
            attempt = 0
            while attempt < n:
                try:
                     return func(*a, **b)
                except Exception as e:
                    attempt +=1
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == n:
                        print(f"maximum Attempt {attempt} Failed :")
                        raise
                    else:
                        print(f"retying... {attempt}..../n")
                        time.sleep(2)
        return inner_decorator
    return decorator


@retry(3)
def guess():
    if random.random() < 0.9:
        raise ValueError("Random failure occurred.")
    print("Success...")

guess()