# # Create a Class.....................
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         name = self.name
#         age = self.age
#         print(name, age)
#
# #Create Object.....................................
# tamim = Student("Tamim", 18)
# tamim.info()


##Constructor Method....................
# class Student:
#     def __init__(self, name): #Constructor
#         print(f"This is a {name} Function That are Automatically called into create Object")
# cons = Student("Construct", ) #Object


# #Constructor Method.........................
#
# class Student:
#     def __init__(self, name, age, subject):
#         self.name = name
#         self.age = age
#         self.subject = subject
#
#     def infor(self ):
#         print(f"student Name is {self.name}, They Are  {self.age} Years old, He is Collect {self.subject} Book")
#
# rahul = Student("Rahul", 21, "Python")
# tamim = Student("Tamim", 25, "Python-3")
#
# rahul.infor()
# tamim.infor()

# #Constructor Method --> Change Class Value...........................
#
# class Student:
#     def __init__(self):
#         self.name = 'Student'
#         self.age = 21
#
# rahul = Student()
# print(rahul.name)
# chng_name = rahul.name =  "Tamim"
# print(chng_name)


# #Diferent Type Of Attibute.................................................
# #Create Diferent type Attibute
# class Student:
#     name = "Tamim"  # 👉 Class Attribute
#
#     def __init__(self, name):
#         self.name = name  # 👉 Object Attribute
#         self.age = 25     # 👉 Another Object Attribute
#
#     def showname(self):
#         print("Object Attribute Name:", self.name, self.age)
#
# # 👉 Create object
# tamim = Student("Tamim, this is Object Attribute")
#
# # 👉 Access Object Attribute through method
# tamim.showname()  # এই লাইন প্রিন্ট করবে, কিন্তু return কিছু করছে না
#
# # 👉 Access Class Attribute directly from class
# print("Class Attribute Name:", Student.name)


# #Diferent Type Of Method .................................................
# #Instance Method (With Self)
#
# class Student:
#     def info(self):
#         print("This is a Instance Method")
# instance = Student()
# instance.info()

# #Class Method ( With Cls)
# class Student:
#     school = "ABC Scholl"

#     @classmethod
#     def class_method(cls, name, age, school):
#         cls.school = school
#         print(f"This is a Class Method {name} & Age {age} , School Name  = {cls.school}")

# Student.class_method("My Name Is Tamim", 25, "Plashbari SM pilot High School")

# #Static Method ( Without Self, cls)
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @staticmethod
#     def static_method( ):
#         print("Static method")


# #Access Object Based
# obj = Student("John", 36)
# obj.static_method()
#
# #Access Class Based
# Student.static_method()



# #Delete Object Wising Del() Keywpord.......................................
# class Student:    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age        
#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
# # Create an object
# rahul = Student("Rahul", 21)  
# # Access the object's info method
# print("Object created successfully")
# rahul.info()      
# # Delete the object using del keyword
# del rahul
# print("Object deleted successfully")

# #Privete and Public Method........................................
# class Student:
#     def __init__(self, name, age):
#         self.name = name  
#         self.age = age
#     def public_method(self):
#         print(f"Public Method: Name: {self.name}, Age: {self.age    }")  
#     def __private_method(self):
#         print(f"Private Method: Name: {self.name}, Age: {self.age}")
#     def access_private_method(self):
#         self.__private_method()  # Accessing private method within the class
# # Create an object
# rahul = Student("Rahul", 21)  
# # Access public method
# rahul.public_method() 
# # Access private method using public method
# rahul.access_private_method()
# # Attempt to access private method directly (will raise an error)

