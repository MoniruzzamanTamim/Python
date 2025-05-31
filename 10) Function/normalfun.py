


def sum_Number():
    a = 20
    b = 20
    sum = a + b 
    print(sum)
    return sum
sum_Number()


def sum_number():
    a = 10
    b = 12
    sum = a+b
    return sum
x = sum_number()
print(x)


#USE Funcition with Perameter and Inner Value || NO Argument Work in this Case
def sum_NumbER(a,b):
    a = 10
    b = 20
    return a, b
a,b = sum_NumbER(0,0)
sum = a+b
print(sum)

#Use Perameter & Argument on Function 

def avg_number (a,b,c):
    avg = a+b+c/3
    return avg 

result= avg_number(10,12,18)
print(result) 


def grade(avg):
    if avg >=80:
        return "A+"
    elif avg>=70:
        return "A"
    elif avg > 50:
        return "F"


sub1 = 80
sub2 = 70
sub3 = 60
total =sub1+sub2+sub3
avg = total/3
grade = grade(avg)

print(grade)


#dEFAULT PERAMETER vALUE

def cal_name(name = "Tamim"):
    print(name)

cal_name()

def cal_name(firstName = "Tamim", lastName="jibin"):
    print("FirstName", firstName)
    print("LastName", lastName)

cal_name()



def Default_perameter(name,age=20):
    print(name,age)

Default_perameter("Tamim")