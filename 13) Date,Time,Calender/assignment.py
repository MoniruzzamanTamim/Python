from datetime import datetime, timedelta, time

now = datetime.now()
print("Current Date:", now.strftime("%d %B, %Y"))
print("Current Time:", now.strftime("%I:%M %p"))


#Birth Year Calculation 
# Birth_year =  input(" Enter your birthday (dd-mm-yyyy: ")
# convert_dateobj = datetime.strptime(Birth_year,  "%d-%m-%Y")

# total_age = now - convert_dateobj
# print("Total Age : ", total_age.days//365 , "years") 

#Current Days  er sathe 10Days + & 1
next = now + timedelta(days=10)
print("Next 10 Days:",next.strftime( "%d %B, %Y"))
front = now - timedelta(days=10)
print("Front 10 Days:",front.strftime( "%d %B, %Y"))

#✅ Assignment 4: ইউজার সময় দিবে (HH:MM), সেটি থেকে ২ ঘণ্টা যোগ করো
# userinput = input("Type Your Time :  (HH:MM) : ")
# convert_userinput = datetime.strptime(userinput,  "%H:%M")
# finall_result = convert_userinput+ timedelta(hours=2)
# print("Add 2 hous to User input Time: ", finall_result.time())

#✅ Assignment 5: আজ সপ্তাহের কোন দিন তা প্রিন্ট করো
days_name = now.strftime("%A")
print("Today Is: ", days_name)


#Alerm Create 

import datetime
import time
import os  # Optional: sound play for Windows only

# ইউজার থেকে অ্যালার্ম সময় ইনপুট
alarm_time = input("Set alarm (HH:MM:SS format): ")

# অ্যালার্ম রিং হওয়ার আগে চলতে থাকবে
while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current Time:", now, end="\r")  # এক লাইনেই দেখাবে

    if now > alarm_time:
        print("Lower Time Not Allow")
        print("Current Time:", now) 
        break
    elif now == alarm_time:
        print("\n⏰⏰⏰ অ্যালার্ম চলছে! ⏰⏰⏰")
        time.sleep(10)
        # শুধু Windows-এ কাজ করে
        try:
            for i in range(3):
                os.system("start alarm.mp3")  # তোমার system এ mp3 থাকলে চালাবে
                time.sleep(1)
        except:
            print("🔔 Alarm ringing...")
        
        

