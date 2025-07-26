import csv

file_path ="12) File_Handling\\file\\file.csv"

# data = [                                
#     ["Name", "Age", "City"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "Los Angeles"],
#     ["Charlie", 35, "Chicago"]
# ]
# # #✅ 1. normal Way to write data
# try:
#     file_wite = open(file_path, "w", newline="")
#     csv_writer = csv.writer(file_wite)
#     csv_writer.writerows(data)
#     file_wite.close()
#     print("Data written to CSV file successfully.")
# except Exception as e:
#     print(f"Error writing to CSV file: {e}")

# ##✅ 1. normal Way to Read Data from CSV File
# try:
#     file_read =open(file_path, "r")
#     csv_reader = csv.reader(file_read)  
#     for row in csv_reader:
#          print(row)  
#     file_read.close()
#     print(type(row))  # Output: <class 'list'>
# except Exception as e:
#     print(f"Error reading from CSV file: {e}")
    
# #✅ 3. Read CSV as Dictionary
# with open(file_path, "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["Name"], row["Age"],row["City"])  # Accessing by column names
#     print(type(row))  # Output: <class 'dict'>


# #✅ 4. Write CSV with DictWriter

# data = [
#     {"Name": "Tamim", "Age": 25, "Country": "Bangladesh"},
#     {"Name": "John", "Age": 30, "Country": "USA"}
# ]

# with open(file_path, "w", newline="") as file:
#     fieldnames = ["Name", "Age", "Country"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)

#✅ 5. Append Data to CSV
new_row = ["Sara", 28, "Canada"]
with open(file_path, "a+", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)
print("New row appended to CSV file successfully.")