import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # root password থাকলে দিন
    )

    if connection.is_connected():
        print("Database Connected Successfully..........")

    cursor = connection.cursor()

    # ইউজার আগে আছে কিনা চেক করা
    cursor.execute("SELECT COUNT(*) FROM mysql.user WHERE user = 'tamim' AND host = 'localhost'")
    (user_exists,) = cursor.fetchone()

    if user_exists == 0:
        # ইউজার তৈরি করা
        cursor.execute("CREATE USER 'tamim'@'localhost' IDENTIFIED BY 'tamim'")
        cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'tamim'@'localhost'")
        cursor.execute("FLUSH PRIVILEGES")
        print("User created successfully.")
    else:
        print("User 'tamim' already exists.")

except Exception as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
