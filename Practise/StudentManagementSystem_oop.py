class People:
    def __init__(self, name,age,gender):
        self.name =name
        self.age =age
        self.gender =gender

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age} Gender: {self.gender}")

class Student(People):
    def __init__(self,name,age,gender,student_id):
        super().__init__(name,age,gender)
        self.student_id =   student_id
        self.courses ={}

    # def add_Student(self):
    #     print
    def enroll_course(self,course_name):

        if course_name not in self.courses:
            self.courses[course_name] = None
        else:
            print(f"{course_name} is Already Enrolled....")
    def marks(self, course_name,mark):
        if course_name  in self.courses:
            self.courses[course_name] = mark
        else:
            print(f"{course_name} is not Enrolled....")

    def edit_mark(self,course_name, mark):
        if course_name in self.courses:
          self.courses[course_name] = mark
          print(f"Mark Updated Successfully....")
        else:
          print(f"{course_name} is not Enrolled....")

    def display_info(self):
        print(f"Student ID: {self.student_id} || Name: {self.name} || Age: {self.age} || Gender: {self.gender} || ")
        for course,mark in self.courses.items():
            if mark is None:
                print(f"Course: {course} || Marks: Not Assigned || GPA: N/A")
            else:
                    print(f"Course & Mark:  \nCourse: {course} || Marks: {mark} ||")

class StudentManagement:
    def __init__(self):
        self.students ={}

    def add_student(self,student):
        self.students[student.student_id] = student

    def get_student(self,student_id):
        return self.students.get(student_id, "Not Available This Student ")

    def show_all_student(self):
        if not  self.students:
            print("No Students Available...............................")
        else:
            for student in self.students.values():
                student.display_info()
    def delete_student(self,student_id):
        if student_id not in  self.students:
            print("This  Students Not Available...............................")
        else:
           del self.students[student_id]


def main():
    system = StudentManagement()
    while True:
        print(f"Student Management System.. \n1) Add Student: \n2) Edit Student: \n3) Delete Student: \n4) Enroll Course: \n5) Add Marks: \n6) Edit Marks: \n7) Show Student Info: \n8) Show All Student: ")
        option = int(input("Choice an Option: "))
        if option == 1:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Your Name: ")
            age = int(input("Enter Your Age: "))
            gender = input("Enter Your Gender: ")
            student = Student(name,age,gender,student_id)
            # student.marks(course_name,mark)
            student.display_info()
            system.add_student(student)
        elif option == 2:
            student_id = int(input("Enter Student ID: "))
            student = system.get_student(student_id) #Student Id ache ki na ta dekhar jonno
            if student:
                name = input("Enter Your Name: ")
                age = int(input("Enter Your Age: "))
                gender = input("Enter Your Gender: ")
                student = Student(name, age, gender, student_id) #Student Class a argument sent kore
                system.add_student(student) #Student Class Ar Info Alada kore Onno Class A Save Kore
                print("Successfully Updated Student Information")
            else:
                print("NOT Available This Student....  ")

        elif option ==3:
            student_id = int(input("Enter Student ID: "))
            system.delete_student(student_id)

        elif option == 4:
            student_id = int(input("Enter Student ID: "))
            student = system.get_student(student_id)
            if student:
                course_name = input("Enter Your Course Name: ")
                student.enroll_course(course_name) #Student Class er enroll method a argument pass kore.
                print(f"{student_id} Student Successfully Enrolled {course_name} Course")
            else:
                print("NOT Success  ")
        elif option == 5:
            student_id = int(input("Enter Student ID: "))
            student = system.get_student(student_id)
            if student:
                course_name = input("Enter Your Course Name: ")
                mark = int(input("Enter Your Marks: "))
                student.marks(course_name,mark)
            else:
                print("NOT Available This Student....  ")

        elif option == 6:
            student_id = int(input("Enter Student ID: "))
            student = system.get_student(student_id)
            if student:
                course_name = input("Enter Your Course Name: ")
                mark = int(input("Enter Your Marks: "))
                student.edit_mark(course_name,mark)
            else:
                print("NOT Available This Student....  ")


        elif option == 7:
            student_id = int(input("Enter Student ID: "))
            student = system.get_student(student_id)

            if student:
                student.display_info()
            else:
                print("NOT Available This Student....  ")
        elif option == 8:
            system.show_all_student()


main()