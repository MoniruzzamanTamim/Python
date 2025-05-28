
import random
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"
students = {}
menu = {
    1 : "Add Student",
    2 : "Edit Student",
    3 : "Delete Student",
    4 : "View Student",
    5 : "View All Student Data",
    6 : "Exit"
}

while True:
    print("\n===== Student Management System =====")
    for key in menu:
        print(f"{key}: {menu[key]}")
    option = int(input("Enter your choice: "))
    if option == 1:
        id = random.randint(1, 11)
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        print("Enter Your Marks ")
        bangla = int(input("Bangla: "))
        english = int(input("English: "))
        math = int(input("Math: "))
        student = {
                "id": id,
                "name": name,
                "age": age,
                "marks": {
                    "bangla": bangla,
                    "english": english,
                    "math": math,
                }
            }
        students[id]=student
        print("Your Data Updated Successfully... ", "Your ID: ", id)

    elif option == 4:
        student_id = int(input("Enter student ID: "))
        if student_id  in students:
            student = students[student_id]
            print("ID:",student_id)
            print("Name:",student["name"])
            print("age:",student["age"])
            print("Bangla:",student["marks"]["bangla"])
            print("English:",student["marks"]["english"])
            print("Math:",student["marks"]["math"])
            total_mark = student["marks"]["bangla"] + student["marks"]["english"] + student["marks"]["math"]
            avg = student["marks"]["bangla"] + student["marks"]["english"] + student["marks"]["math"]/3
            grade = get_grade(avg)
            print("Total Makrs:", total_mark)
            print("Grade:", grade)

        else:
            print("Student not found... Please Type Wight ID ")
    elif option == 2:
        student_id = int(input("Enter student ID: "))
        if student_id in students:
            student = students[student_id]
            info_edit = True
            while info_edit:
                print("1: Name: ")
                print("2: Age: ")
                print("3: Marks: ")
                print("4: Back Main Menu: ")
                data_up = int(input("Please select: "))
                if data_up == 1:
                    update_name = input("Name: ")
                    student["name"] = update_name
                elif data_up == 2:
                    update_age = int(input("Age: "))
                    student["name"] = update_age
                elif data_up == 3:
                   upd_mark = True
                   while upd_mark:
                        print("subject-List")
                        print("Bangla: ")
                        print("English: ")
                        print("Math: ")
                        print("Done: ")
                        sub_select = input("Please select Subject: ").lower()
                        if sub_select == "bangla":
                            upd_mark = int(input("Type Bangla Mark: "))
                            student["marks"]["bangla"] = upd_mark
                        elif sub_select == "english":
                            upd_mark = int(input("Type English Mark: "))
                            student["marks"]["english"] = upd_mark
                        elif sub_select == "math":
                            upd_mark = int(input("Type Math Mark: "))
                            student["marks"]["math"] = upd_mark
                        elif sub_select == "done":
                            upd_mark = False
                elif data_up == 4:
                    info_edit = False

                else:
                    print("Please Type Write Value...")
            total_mark = student["marks"]["bangla"] + student["marks"]["english"] + student["marks"]["math"]
            avg= student["marks"]["bangla"] + student["marks"]["english"] + student["marks"]["math"] / 3
            grade = get_grade(avg)
            print("Total Marks", total_mark)
            print(grade)

    elif option ==3:
        print("Delete Student Record ==> :")
        student_id = int(input("Enter student ID: "))
        if student_id in students:
            students.pop(student_id)
            print("Student Data Deleted  Successfully ")
        else:
            print("Student not found... Please Type Wight ID ")

    elif option == 5:
        print("View All Student Data ==> :")
        for all_student in students.values():

            for i in range(len(all_student)):
                print( "serial No: ", i , "...........")
                print("ID: ",all_student["id"])
                print("Name: ",all_student["name"])
                print("Age: ",all_student["age"])
                print("Marks:")
                print("Bangla:",all_student["marks"]["bangla"])
                print("English:", all_student["marks"]["english"])
                print("Math:", all_student["marks"]["math"])
                print("Grade: ", grade)
            avg = (all_student["marks"]["english"] + all_student["marks"]["math"]    + all_student["marks"]["bangla"])/3
            grade = get_grade(avg)
            gradeSearch = input("Type Grade: ").upper()
            if  grade ==gradeSearch:
                print(f"\nID: {all_student['id']} | Name: {all_student['name']} | Avg: {avg:.2f} | Grade: {grade}")

    elif option == 6:
        print("Thank You. See Ya!")
        break


