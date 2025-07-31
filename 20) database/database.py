import mysql.connector

try:
    # Step 1: Connect to database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python"   # Ensure this DB exists in phpMyAdmin
    )

    if connection.is_connected():
        print("✅ Connected to database.")

        cursor = connection.cursor()

        # Step 2: Create table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            age INT
        )
        """
        cursor.execute(create_table_query)
        print("🛠️ Table 'users' created (if not exists).")

        # Step 3: Insert sample data
        insert_query = """
        INSERT INTO users (name, email, age)
        VALUES (%s, %s, %s)
        """
        data = [
            ("Tamim", "tamim@example.com", 25),
            ("Amina", "amina@example.com", 22),
            ("Karim", "karim@example.com", 30)
        ]
        cursor.executemany(insert_query, data)
        connection.commit()
        print("✅ Sample data inserted successfully.")

        # Step 4: Show data
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("\n📄 Current Users:")
        for row in rows:
            print(row)

except mysql.connector.Error as err:
    print("❌ Error:", err)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("\n🔌 Connection closed.")
