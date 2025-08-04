import mysql.connector

# Step 1: Connct Database With Database [ iF Already Database Create Thake]
connection = mysql.connector.connect(
    host="localhost",
    user="tamim",
    password="tamim",
    database="university"
)
if connection.is_connected():
    print("Connect Database  Succhessfully..")
else:
    print("Database Not Connected ")

# Step 2: Create Cursor For Execution All Work 
cursor = connection.cursor()

# Step 3: Create Table
try:
    create_table = """
    CREATE TABLE IF NOT EXISTS STUDENTS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    roll INT,
    age INT
    )
    """
    cursor.execute(create_table)
    print("🛠️ Table 'students' created or already exists.")
except Exception as e:
    print("HEllo: ", e)

# Step 4: Close old connection & connect to 'UNIVERSITY' database
cursor.close()
connection.close()

