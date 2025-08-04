# import mysql.connector # Import Database Module


# #Connct Database [IF Database Not Created.....]
# connection = mysql.connector.connect(
#     host="localhost",
#     user="tamim",
#     password="tamim",
# )
# if connection.is_connected():
#     print("Connect Server  Succhessfully..")
# else:
#     print("Database Not Connected ")

# #Create Database Object For Execute All Work 
# cursor = connection.cursor()

# #Create Database 
# try:
#     create_database = """CREATE DATABASE IF NOT EXISTS UNIVERSITY"""
#     cursor.execute(create_database)
#     print("Database Create Successfully....")
# except Exception as e:
#     print(e)

# # Step 3: Close old connection & connect to 'UNIVERSITY' database
# cursor.close()
# connection.close()


# ডাটাবেস আগে থেকে থাকলে → প্রিন্ট করবে "Database already exists"
#ডাটাবেস না থাকলে → তৈরি করবে এবং প্রিন্ট করবে "Database created"

import mysql.connector

db_name = "UNIVERSITY"

# Connect to MySQL Server (Without selecting database)
connection = mysql.connector.connect(
    host="localhost",
    user="tamim",
    password="tamim"
)

cursor = connection.cursor()

# Check if database exists
cursor.execute("SHOW DATABASES")
databases = [db[0] for db in cursor.fetchall()]

if db_name in databases:
    print(f"✅ Database '{db_name}' already exists.")
else:
    cursor.execute(f"CREATE DATABASE {db_name}")
    print(f"🎯 Database '{db_name}' created successfully.")

cursor.close()
connection.close()


# 🔹 কোড ব্যাখ্যা
# SHOW DATABASES → সব ডাটাবেস লিস্ট আনে
# List comprehension দিয়ে শুধু নাম বের করা → [db[0] for db in cursor.fetchall()]
# যদি নাম মিলে যায় → "already exists"
# না মিললে → CREATE DATABASE করে