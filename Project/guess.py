import random


change = 7
guesses = 0
random_num = random.randint(1,10)

while change >= guesses:
    guesses +=1
    
    try:
        num = int(input("Guess Your Number(1-10): "))
        if random_num ==num:
            print(f"Congratulations......!\nYour guesses Number was a Correct , Your : {num} & Random Number: {random_num} is Correct")
            break
        elif change <= guesses and random_num != num:
            print(f"You Are try Many More Time, Please Try Next Time... Good Luck!\nYour Guesses Number is {num} but Random Number is {random_num} , Not Correct")
            break

        elif random_num > num:
            print(f"Too High!...\nYour Guesses Number is {num} but Random Number is {random_num} , Not Correct Try Agaign....")
        elif random_num < num:
            print(f"Too Low!....\nYour Guesses Number is {num} but Random Number is {random_num} , Not Correct Try Agaign....")
    
    except ValueError:
        print("Please Type Only Integer Number.....Thank You! ")

