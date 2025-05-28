students = []
student_id = 1

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        math = int(input("Enter Math marks: "))
        science = int(input("Enter Science marks: "))
        english = int(input("Enter English marks: "))

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "marks": {
                "math": math,
                "science": science,
                "english": english
            }
        }

        students.append(student)
        print(f"✅ Student {name} added successfully!")
        student_id += 1

    elif choice == "2":
        if not students:
            print("⚠️ No students found.")
        else:
            for s in students:
                avg = sum(s["marks"].values()) / 3
                print(f"\nID: {s['id']} | Name: {s['name']} | Age: {s['age']}")
                print(f"Marks: {s['marks']} | Average: {avg:.2f}")

    elif choice == "3":
        print("Exiting program... 👋")
        break

    else:
        print("❌ Invalid option. Please choose 1, 2, or 3.")
