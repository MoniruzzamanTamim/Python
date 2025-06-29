#Polyphesm Mean Same Type Methd of Diferent classes



class A:
    name = "Tamim"
    age = 25
    @staticmethod
    def info():
        print(A.name, A.age)

class B(A):
    institute = "CUB"
    sub = "CSE"
    @staticmethod
    def info():
        print(B.name, B.age)

class C(B):
    code = 2158
    @staticmethod
    def info():
        print(C.code)


alls= [ 
       A(),
       B(),
       C()
       ]

for all in alls:
    all.info()