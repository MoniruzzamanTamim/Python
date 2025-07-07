#Basic Decorator

def decorator(main_func): #Create Decorator and receive Main Function

    def inner_decorator():
        #PreAction 
        print("PreAction:  Main function kaj korar age ki korte chai seta")
        main_func()  #Call Main Function 
        #PostAction
        print("PostAction:  Main function kaj korar por  ki korte chai seta")
    
    return inner_decorator 

# #ডেকোরেটর ব্যবহার (Without @ symbol):.....................................................
# #First Create  Main F unction
# def main_func():
#     print("Main Function: Working Main Funtion....")
# #Second Use Decorator
# use_decorator = decorator(main_func)
# print(use_decorator())

#✨ ডেকোরেটর ব্যবহার (With @ symbol):...............................................................
@decorator
def main_func():
    print("Main Function: Working Main Funtion....")

print(main_func())





#Practise Decorator ....................................... Create a Project 
"""✅ প্রজেক্ট আইডিয়া: Secure Function Access System
আমরা এমন একটি সিস্টেম তৈরি করব যেখানে কিছু ফাংশনে অ্যাক্সেস পাওয়ার জন্য পাসওয়ার্ড লাগবে।
এই নিরাপত্তা (security) ফিচারটি আমরা ডেকোরেটর দিয়ে তৈরি করব।
🎯 ফিচারসমূহ:
ইউজার ফাংশন কল করলে, ডেকোরেটর চেক করবে ইউজার পাসওয়ার্ড দিয়েছে কি না।
যদি পাসওয়ার্ড ঠিক থাকে, তাহলে ফাংশন চলবে।
ভুল পাসওয়ার্ড দিলে – "Access Denied" দেখাবে।"""

print("Project 1 ........................................................")
from functools import wraps

def use_pass(main_func):
    @wraps(main_func)
    def innerdecorate(*args, **kwargs):
        password = input("Type Your Password: ")
        if  password == "tamim12":
            print("Access Granted....")
            return main_func(*args, **kwargs)
        else:
            return "Access Denide................."
    return innerdecorate


#Use Decorate  
@use_pass
def user_info(name,age,balance):
    print(f"User Name is {name}, User Gae is {age} and User Blance Available {balance}")

#Use Decorate  
@use_pass
def transfer_money():
    print("💸 Transferring money...")


#Public function Not Use Decorator 
def hello():
    print("Say Hello....")


def main():
    print("\n")
    while True:
        print("1) Check user Info \n2)Transfer Money \n3)Sey Hello \n4)Exit")
        option = int(input("Choice an Option: "))
        if option == 1:
            user_info("Tamim", 25, 25804)
        elif option ==2:
            transfer_money()
        elif option ==3:
            hello()
        elif option == 4:
            break
        else:
            print("Invalid option")


main()

print("\n")
print("Project-2........................................................................")
"""✅ প্রজেক্ট নাম: custom_logger
🎯 লক্ষ্য:
একটি ডেকোরেটর তৈরি করবো যেটা যেকোনো ফাংশনের নাম
প্যারামিটার *args, **kwargs
টাইম
রিটার্ন ভ্যালু
👉 সব কিছু একটি .txt ফাইলে লগ করবে।
"""

import datetime
from functools import wraps

def logmessage(main_func):
    @wraps(main_func)
    def innerDecorator(*args,**kwargs):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Date & Time Genaret
        name= main_func.__name__  #collect Main_function Named
        result = main_func(*args,**kwargs)   #Main Function Assign
        
        log = (
           f" [{time}] Function '{name}' called.\n" 
                f"  Arguments: args={args}, kwargs={kwargs}\n"
                f"  Returned: {result}\n"
                "-----------------------------\n"
        ) 
        log_file_path = "14) Decorator\\log.txt"
        with open(log_file_path, "a") as file:
            file.write(log)
            
        return result
    return innerDecorator



@logmessage
def  info(name,age):
    print(f"hello {name}, age {age} , Your Login Information are Store log.txt File SuccessFully")
    return f"hello {name}, age {age}"

info("TAMIM",age =254)