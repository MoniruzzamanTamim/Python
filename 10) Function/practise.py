
def greet(name):
    print("name:-", name)

greet("Moniruzzaman")




def add(a,b):
    sum = a+b
    return sum

result = add(5,10)
print(result)



def is_even(n):
    if n%2==0:
        return "This is Even Number"

n = int(input("Type Your Number: \t"))
print(is_even(n))


def introduce(name, country="Bangladesh"):
    return ""f"{name} lives in {country}"""

print(introduce("Tamim"))

def introduce(name, country="Bangladesh"):
    return ""f"{name} lives in {country}"""

print(introduce("Tamim", "USA"))




def power(base,  exponent=2):
    power_number = base**exponent
    return power_number


result = power(3)
print(result)


item = [("Burger", 120), ("Pepsi", 30)]

def calculate_bill(name,items):
    total =0
    for item in items:
        total +=item[1]
    print(total)
calculate_bill("Moniruzzaman", item)