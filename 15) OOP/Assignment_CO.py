class Student:
    # ✅ Class Attribute
    school = "ABC School"

    # ✅ Constructor (__init__) – Object Attribute set করে
    def __init__(self, name, roll):
        self.name = name         # Object Attribute
        self.roll = roll         # Object Attribute

    # ✅ Instance Method
    def show_info(self):
        print("Name is:", self.name)
        print("Roll is:", self.roll)
        print("School Name is:", Student.school)
        print("--------------------------")

    # ✅ Class Method
    @classmethod
    def change_school(cls, school_name):
        cls.school = school_name
        print("School name changed to:", cls.school)

    # ✅ Static Method
    @staticmethod
    def is_valid_roll(roll):
        return isinstance(roll, int)


# ✅ Creating Objects
tamim = Student("Tamim", 25)
iqbal = Student("Iqbal", 28)

# ✅ Showing Student Info
tamim.show_info()
iqbal.show_info()

# ✅ Accessing Class Attribute
print("Current School Name:", Student.school)

# ✅ Changing School Name using Class Method
Student.change_school("SM Pilot High School")

# ✅ Showing updated school name
tamim.show_info()
iqbal.show_info()

# ✅ Using Static Method
print("Is 100 a valid roll number?", Student.is_valid_roll(100))
print("Is 'ABC' a valid roll number?", Student.is_valid_roll("ABC"))


print(F"\n \n")
print("Assingment 2...........")

class Employee:
    company = "TechSoft"
    def __init__(self, name,id,department):
        self.name = name
        self.id = id
        self.department = department
    def show_info(self):   #Instace Method
        print("Name is:", self.name)
        print("Id is:", self.id)
        print("deaertment is: ", self.department)
        print("Company is:", Employee.company)
        print(".........................................................................")
    @classmethod
    def change_company(cls, cmp_name):  #Class Method 
        cls.company = cmp_name
        print("Company changed to:", cls.company)

        print(".........................................................................")
    @staticmethod
    def is_valid_id(id):  #Static Method 
        print(F"your Id {id} is a Valid", isinstance(id, int))
        print(".........................................................................")


hyder = Employee("Hyder", 258, "CSE")
hyder.show_info()
print("Current Company Name:", Employee.company)
Employee.change_company("X-Press Technology LTD")

print("After Change Comapny ..............")
hyder.show_info()

Employee.is_valid_id(258)


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
