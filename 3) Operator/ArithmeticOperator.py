print( "\t \t Arithmetic Operator \t \t")


number1 = 10
number2 = 25
number3 = 2
number4 = 3


addition = number1+number2
Substraction = number2-number1
multiplication= number1*number3
divition = number1/number4
exponention = number3**number4
floor = number1//number4
module = number2%number4



print("Addition =", addition)

print("Substraction: ", Substraction)
print("Multiplication: ", multiplication)
print("Divion: ", divition)
print("Module: ", module)
print("Floor: ", floor)
print("Exponention: ", exponention)





# Priority
result = (number3**number4-number4 /number1)+ number3**2
print(result)




#Math Function On Python 

import math 
num = 5 
num2 = -4.8
num3 = 4.8
num4 = 14.2

print("Power", math.pow(num,2))
print("PI:" , math.pi)
print("ABS: ", abs(num2))
print("Ceil: ", math.ceil(num3)) 
print("Floor: ", math.floor(5/2))
print("Floor: ", math.floor(num3))
print("MINimum : ", min(10,5))
print("Maximum : ", max(10,5))
print("Round", round(num4))


import random
print("Random Number:", (random.random()))
print("Randiant :", random.randint(1,2)+random.randint(1,6))
print("Uniform:", random.uniform(1,6))



#Advanced Min(), Max() 
words = ["Python", "is", "awesome"]
longest = max(words, key=len)
print("Longerst Word: ", longest)  # awesome

expenses = [
    {"item": "Food", "amount": 200},
    {"item": "Transport", "amount": 150},
    {"item": "Shopping", "amount": 300}
]
#এখন সবচেয়ে বেশি খরচের রেকর্ড বের করতে:

highest = max(expenses, key=lambda x: x["amount"])
print("highest",highest)

#এখন সবচেয়ে কম খরচের রেকর্ড বের করতে:
lowest = min(expenses, key=lambda x: x["amount"])
print("highest", lowest)