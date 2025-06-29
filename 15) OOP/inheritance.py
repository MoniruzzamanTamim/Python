

#Inheritance allows us to define a class that inherits all the methods and properties from another class.
class Car: #Base class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

    @staticmethod
    def start_engine():
        print("Car Engine started!")
    @staticmethod
    def stop_engine():
        print("Car Engine stopped!")

class ElectricCar(Car): #Child Case 
    
    def __init__(self):
        pass
    
    @staticmethod
    def  function():
        print("Car Ready ")

#Create Object For Child Class

car =Car("Toyota", "CS")
el =ElectricCar()
el.function()
car.start_engine()  #Access Base Class Method On Child Class 
car.display_info()
car.stop_engine()  #Access Base Class Method On Child Class 


print("Hello")