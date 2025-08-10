

def add():
    sum = 10+10
    print(sum)




class Calculator:
    def __init__(self):
        pass
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def minus(a,b):
        return a-b
    @staticmethod
    def multiply(a,b):
        return a*b
    @staticmethod
    def divide(a,b):
        if a == 0 and b == 0:
            raise ValueError("Can't Devide By Zero")
        return a/b
    

cal = Calculator()
print(f""" 
{cal.add(10,10)}
{cal.minus(10,10)}
{cal.multiply(15,10)}
{cal.divide(10,100)}
""")



def string_test():
    name = "Tamim"
    return name

def number_test():
    id = 123456
    return id






