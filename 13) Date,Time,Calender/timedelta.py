from datetime import datetime, timedelta




timedelta_function = timedelta(days=10)
now = datetime.today()
print("Plus 8 Days Using Timedelta:", now + timedelta(days=8))
print("Plus 8 & 5 Hour Days Using Timedelta:", now + timedelta(days=8, hours=5))
print("Plus 8 Days Using Timedelta:", now + timedelta(days=8, hours=5, minutes=50))

#Use Year & Month 
from datetime import datetime
# # from dateutil.relativedelta import relativedelta
# import dateutil

# today = datetime.now()
# after_1_year_2_months = today + relativedelta(years=1, months=2)
# print("আজ:", today.strftime("%d %B %Y"))
# print("১ বছর ২ মাস পর:", after_1_year_2_months.strftime("%d %B %Y"))


#Birth Year Calculate
birthday = "8 September, 2000 04:00 PM"
convert_dateobj = datetime.strptime(birthday, "%d %B, %Y %I:%M %p")
print(convert_dateobj)
now = datetime.now()
total_age = now - convert_dateobj
print("total age: ", total_age )
print("total Days: ", total_age.days)
print("total Month: ", total_age.days//30)
print("total Year: ", total_age.days//365)