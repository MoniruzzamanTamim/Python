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
