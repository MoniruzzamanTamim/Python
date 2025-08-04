import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "tamim",
    password = "tamim",
    database = "university"
)

if connection.is_connected():
    print("Connect Database, Table,  Succhessfully..")
else:
    print("Database Not Connected ")


# Create Cursor for All Work Execution 
cursor = connection.cursor()

# # Create Data And Submit to Database Table  ==> Normal Way To Insert Data 
# insert_data = """
# INSERT INTO STUDENTS (name, roll, age)
# VALUES
# ('Tamim', 25, 25),
# ('Iqbal', 30, 30)
# """ 
# cursor.execute(insert_data)
# connection.commit()  # ✅ এটা না দিলে data সেভ হবে না
# print("✅ Data Insert Completed")


# Create Data And Submit to Database Table  ==> Use Advance Way 

query = "INSERT INTO STUDENTS (name, roll, age) VALUES (%s, %s, %s)"
students = [
    ("Tamim", 101, 21),
    ("Sadia", 102, 22),
    ("Karim", 103, 23),
    ("Rahim", 104, 24),
    ("Nusrat", 105, 20),
    ("Rafi", 106, 25),
    ("Fahim", 107, 26),
    ("Tania", 108, 21),
    ("Shuvo", 109, 23),
    ("Anika", 110, 22),
    ("Mitu", 111, 24),
    ("Hasib", 112, 22),
    ("Zara", 113, 23),
    ("Nabil", 114, 25),
    ("Tanvir", 115, 21),
    ("Elma", 116, 20),
    ("Jamal", 117, 26),
    ("Kamal", 118, 22),
    ("Sajib", 119, 23),
    ("Lubna", 120, 24),
    ("Arif", 121, 22),
    ("Rupa", 122, 21),
    ("Shamim", 123, 24),
    ("Borna", 124, 20),
    ("Farhan", 125, 23),
    ("Mahi", 126, 22),
    ("Adnan", 127, 25),
    ("Rumi", 128, 21),
    ("Tuhin", 129, 26),
    ("Samiha", 130, 23),
    ("Imran", 131, 22),
    ("Sumaiya", 132, 24),
    ("Parvez", 133, 25),
    ("Shakil", 134, 20),
    ("Joti", 135, 21),
    ("Fariha", 136, 22),
    ("Rakib", 137, 23),
    ("Afia", 138, 24),
    ("Sajjad", 139, 26),
    ("Promi", 140, 22),
    ("Sakib", 141, 21),
    ("Rebeka", 142, 20),
    ("Mamun", 143, 25),
    ("Popy", 144, 23),
    ("Shanto", 145, 24),
    ("Minhaj", 146, 22),
    ("Kazi", 147, 21),
    ("Nadim", 148, 26),
    ("Shama", 149, 23),
    ("Milton", 150, 25),
    ("Sharmin", 151, 24),
    ("Rubel", 152, 22),
    ("Shila", 153, 20),
    ("Rony", 154, 23),
    ("Priya", 155, 21),
    ("Asif", 156, 26),
    ("Shabnam", 157, 22),
    ("Tarek", 158, 25),
    ("Munia", 159, 24),
    ("Aziz", 160, 20),
    ("Hira", 161, 23),
    ("Biplob", 162, 21),
    ("Nargis", 163, 22),
    ("Selim", 164, 25),
    ("Moni", 165, 24),
    ("Ovi", 166, 20),
    ("Moushumi", 167, 23),
    ("Shuvo", 168, 26),
    ("Bashir", 169, 22),
    ("Parvin", 170, 21),
    ("Sohan", 171, 25),
    ("Chayan", 172, 23),
    ("Fahima", 173, 22),
    ("Shakila", 174, 20),
    ("Zubair", 175, 24),
    ("Nahid", 176, 26),
    ("Mim", 177, 21),
    ("Shaila", 178, 25),
    ("Borna", 179, 22),
    ("Tanisha", 180, 20),
    ("Jahid", 181, 23),
    ("Lamia", 182, 24),
    ("Sohanur", 183, 26),
    ("Rashed", 184, 21),
    ("Tasnim", 185, 22),
    ("Milon", 186, 25),
    ("Sumon", 187, 23),
    ("Anwar", 188, 20),
    ("Keya", 189, 24),
    ("Afsana", 190, 21),
    ("Sumi", 191, 26),
    ("Shafik", 192, 22),
    ("Bappy", 193, 25),
    ("Omar", 194, 20),
    ("Sajida", 195, 23),
    ("Tania", 196, 24),
    ("Mehedi", 197, 21),
    ("Masud", 198, 26),
    ("Rafsan", 199, 25),
    ("Sadia", 200, 22)
]

cursor.executemany(query, students)
connection.commit()  # ✅ এটা না দিলে data সেভ হবে না
print("✅ Data Insert Completed")

cursor.close()
connection.close()
