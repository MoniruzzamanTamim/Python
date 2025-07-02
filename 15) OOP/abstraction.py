#it's means Hide Inner Function, Just Show Working Function 


from abc import ABC, abstractmethod

import math

class Sharp(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def test(self):
        pass
    
class Circle(Sharp): 
    def __init__(self, num):
        self.num = num
    def area(self):
        return   math.pi  * self.num ** 2
    @staticmethod
    def test():
        print("Circle Class IS Define......")


class Rectangle(Sharp):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    def area(self):
        return  self.height * self.weight 
    @staticmethod
    def test():
        print("Rectangle Class IS Define......")

class Triangles(Sharp):
    def __init__(self, base,height):
        self.base =base
        self.height =height
    def area(self):
        return  0.5*self.base*self.height

    @staticmethod
    def test():
        print("Triangles Class IS Define......")

#Access Abstraction &  Polymerphim
sharps = [
Circle(5),
Rectangle(10,4), 
Triangles(6, 4)
]

for sharp in sharps:
   print( sharp.area())

for t in sharps:
    t.test()