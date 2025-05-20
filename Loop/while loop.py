
#Basic While

i = 1
while i<10:
    print(i)
    i+=1

#infinity Loop
name =""
while True:
    name = input("Enter your name: ").lower()
    if name =="tamim":
        print(name , "Program is Stop Forcefully Using Break Statement....")
        break
    else:
        print(" 'program is infinity'")

#Else Cause

i = 1
while i<=5:
    print(i)
    i+=1
else:
    print("else Cause While Loop")

# Break Statement

digit = 1
while digit < 6:
    if digit==4:
        print(digit)
        break
    else:
     print(digit)
     digit += 1

print("........................")
#Continue Statement
digit2 = 1
while digit2 < 6:
    if digit2 == 4:
        print(f"Skipping: {digit2}")
        digit2 += 1
        continue
    print(digit2)
    digit2 += 1
