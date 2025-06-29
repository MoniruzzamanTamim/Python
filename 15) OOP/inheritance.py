

# #Inheritance allows us to define a class that inherits all the methods and properties from another class..............................................
# class Car: #Base class
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         print(f"Car Brand: {self.brand}, Model: {self.model}")

#     @staticmethod
#     def start_engine():
#         print("Car Engine started!")
#     @staticmethod
#     def stop_engine():
#         print("Car Engine stopped!")

# class ElectricCar(Car): #Child Case 
    
#     def __init__(self):
#         pass
    
#     @staticmethod
#     def  function():
#         print("Car Ready ")

# #Create Object For Child Class

# car =Car("Toyota", "CS")
# el =ElectricCar()
# el.function()
# car.start_engine()  #Access Base Class Method On Child Class 
# car.display_info()
# car.stop_engine()  #Access Base Class Method On Child Class 

# #⇒ চাইল্ড ক্লাস  এ যদি কন্সট্রাকটর ব্যাবহার না করি এবং প্রারেন্ট ক্লাসের মাঝে কন্সট্রাকটর ও প্যারামিটার থাকে   
# # তাহলে চাইল্ড ক্লাস কে কল করার  সময় প্রারেন্ট  ক্লাসের কন্সট্রাকটর ও প্যারামিটার  এর জন্য  চাইল্ড ক্লাস থেকেও আর্গুমেন্ট বা ভ্যালু সেট করে দিতে হবে । .............................................................
# class School():
#     sch_name = "Plashbari SM Pilot Govt. High School"
#     def __init__(self, code, shift):
#         self.code = code
#         self.shift= shift
#     def show_info(self):
#         print(f"School Name : {School.sch_name}, School Code {self.code} and there are {self.shift} Shift Available  ")
# class Student(School):
#     @staticmethod
#     def  stdentinfo():
#         print("Child Class No Use Constructor,  And Parent Use Construct and Perameter , So Child Call time Set Perameter Vallue from Child Class")

# school = School(2,5) # Call Parent Class With  Argument
# student = Student(100,258) #Call Child Class with Argument Must 
# student.stdentinfo() 


#Super( ) Function ...............................................

class  University:
    info = "Hello! Please Share your Information "
    def __init__(self, name, location):
        self.name =name
        self.location = location
    def show_info(self):
        print(f"University Name: {self.name} \n Location: {self.location}")

class Depertment(University):
    
    def __init__(self, name, location,depertmentName):
        super().__init__(name, location)
        self.depertmentName = depertmentName
    
    def show_info(self):
        super().show_info()
        print(f"DepertMent: {    self.depertmentName }")
    
# print("Hello")
class Student(Depertment): 
    
    def __init__(self, name, location,depertmentName,student_name, roll):
        super().__init__(name, location,depertmentName)
        self.student_name = student_name
        self.roll = roll
    def show_info(self):
        super().show_info()
        print(f"Student Name: { self.student_name } \n Student Roll: {self.roll} ")

tamim =Student ("CUB", "Badda","CSE","Tamim", 23105036)
tamim.show_info()


