
from datetime import datetime  
#today() function

today = datetime.today()
print("Today:", today)
now = datetime.now()
print("Now All: " , now)
print("Only Date:", now.date())
print("Only Time:", now.time())

print("Year:", now.year)
print("Month:", now.month)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

#create Custom Date & time 
custom_Date = datetime(2025,5,10)
print("Set Custom Date & Time:", custom_Date)
custom_All = datetime(2025,5,10,10,25,58)
print("Set Custom Date & Time:", custom_All)

#Custom Time Configure
from datetime import time

t = time(15, 30, 45)
print("Set Custom Time:",t)                 # 15:30:45
print("Set Custom Hour:",t.hour)            # 15
print("Set Custom Minute:",t.minute)          # 30
print("Set Custom Second:",t.second)          # 45








#Calender Module
import calendar

month = calendar.month(2025,6)
print(month)




html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
print(html_cal.formatmonth(2025, 6))
