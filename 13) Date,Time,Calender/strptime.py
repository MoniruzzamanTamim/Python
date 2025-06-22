from datetime import datetime
from datetime import date

birthday = "15 May, 2000"
print(birthday, type(birthday))
convert_dateObj = datetime.strptime(birthday, "%d %B, %Y")
print(convert_dateObj.date(), type(convert_dateObj))
