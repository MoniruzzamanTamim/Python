import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "tamim",
    password = "tamim",
    database = "university"
)

if connection.is_connected():
    print("Database Connect Successfully.........")


#Create Database Object (Cursor) For All Work Execution: 
cursor = connection.cursor()
show_data = "select * from  Students "
cursor.execute(show_data)
allData = cursor.fetchall()
for data in allData:
    print(f"ID: {data[0]} || Name: {data[1]} || Roll:{data[2]} ||  Age: {data[3]}" )
    print(type(data))


cursor.close()
connection.close()
