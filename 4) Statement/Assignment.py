#1. Check if a number is positive, negative, or zero.
#Write a program that takes an integer input and prints whether it is positive, negative, or zero.

# num = " "
# while num !='limit':
#     num = int(input("Type Your Number:\t"))
#     if num == 0:
#        print("number is a Zero")
#     elif num > 0:
#        print("Number is a Positive Number")
#     elif num < 0 :
#        print("Number is a Negetive")
#     else:
#        print("Wrong Number")


# 2. Odd or Even
# Write a program that asks the user to input a number and prints whether it is even or odd.

# num = " "
# while num != 10:
#     num = int(input("type your Number : \t "))
#     if num%2==0:
#         print("This is a Even Number")
#     elif num%2!=0:
#         print("This is a ODD Number")
#     else:
#         print("This is Negetive Number")

# 3. Find the largest of two numbers
# Take two numbers from the user and print which one is greater. If both are equal, print "Both are equal".


# x = int(input("Please Type 1st Number:\t  "))
# y = int(input("Please Type 2nd  Number:\t "))

# if x > y : 
#     print("1st Number is a Greater Number ")
# elif x < y : 
#     print("2st Number is a Greater Number ")
# elif x==y:
#     print("1st & 2nd both number are Equal")


# 4. Grade Checker
# Take a number input from 0 to 100 and print the grade based on the following:

# 90-100: A   80-89: B  70-79: C 60-69: D   Below 60: F


# mark = int(input("Type your Marks\t "))

# if mark >=90:
#     print("Your Mark:", mark, "Grade A")
# elif mark >=80:
#     print("Your Mark:", mark, "Grade B")
# elif mark >=70:
#     print("Your Mark:", mark, "Grade C")
# elif mark >=60:
#     print("Your Mark:", mark, "Grade D")
# elif mark <60:
#     print("Your Mark:", mark, "Grade F")


# 5. Check Leap Year
# Write a program that checks whether a given year is a leap year or not. (Hint: Use divisible by 4, 100, and 400 rules.)

# year = int(input("Type your Year:\t "))

# if year%4==0:
#     print("This is Leap Year")
# else:
#     print("This is not Leap Year")


# Ternary Operator ==> Same As If...Else Statement 

# number = 40
# result = 10 if number >= 30 else 'fail'
# print(result)

Result = "Pass" if 50+20==70 else "Fail" 
print(Result)


# Nested Statement

number = 1

# outer if statement
if number >= 1:
    # inner if statement
    if number == 0:
        if number+5==6:
            print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')