def add_student(students, name, marks):
    students.append({"name": name, "marks": marks})
    return students

def average_marks(students):
    total = sum(s["marks"] for s in students)
    avg = total / len(students)
    return avg

def top_student(students):
    highest = max(students, key=lambda s: s["marks"])
    return highest

if __name__ == "__main__":
    students = []
    
    # Breakpoint 1
    import pdb; pdb.set_trace()

    add_student(students, "Amin", 80)
    add_student(students, "Rafi", 90)
    add_student(students, "Nila", 85)

    # Breakpoint 2
    import pdb; pdb.set_trace()

    avg = average_marks(students)
    top = top_student(students)

    print("Average Marks:", avg)
    print("Top Student:", top)
