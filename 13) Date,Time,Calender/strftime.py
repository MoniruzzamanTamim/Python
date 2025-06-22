from datetime import datetime

now = datetime.today()
print("Normal Way to Present Date & Time:", now)

#Using Strftime to Formating Date & Time


date_name = now.strftime("%a, %A , %b, %B, %c, %d, %H, %I, %j, %m, %M, %p, %S, %U, %w, %W, %x, %X, %y, %Y, %Z")
print(date_name)
