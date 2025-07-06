# import os
# import json
# data = {
#     "name": "Tamima",
#     "age": 25,
#     "location": {
#         "country": "Bangladesh",
#         "city": "Dhaka"
#     },
#     "languages": ["English", "Bengali"]
# }

# file_path ="12) File_Handling\\file\\json.json"

# #View Data On Exiting File ==> Normal Way 
# import os
# if os.path.exists(file_path):
#     with open(file_path, "r") as r:
#         read_data = r.read()
#         print(read_data)
#         print(type(read_data))
# else:
#     print("please Type valid File Path")



# #View Data On Exiting File ==>Convert Dict 
# if os.path.exists(file_path):
#     with open(file_path, "r") as r:
#         read_data = json.load(r)
#         print(read_data)
#         print(type(read_data))
# else:
#     print("please Type valid File Path")


# #Sent Dict Data-Type To Store Using File Handling
# import json
# if os.path.exists(file_path):
#     with open(file_path, "a") as w:
#         json.dump(data,w, indent=4)
#         print("Your Data Sent Successfully")
# else:
#     print("please Type valid File Path")




# import os
# import json

# # 🔹 Step 1: Data to be stored
# list_data = [
#     {"name": "Tamima", "age": 25},
#     {"name": "Rahim", "age": 30}
# ]

# # 🔹 Step 2: File path

# # 🔹 Step 3: Store data (overwrite or merge if file exists)
# if os.path.exists(file_path):
#     with open(file_path, "w") as w:
#         json.dump(list_data, w)
#         print("Data load Successfully")
# else:
#     print("Your Process Wrong")
    
# print("\n📄 Showing JSON File Data:")


# # 🔹 Step 6: Show Data
# print("\n📄 Showing JSON File Data:")
# with open(file_path, "r") as file:
#     try:
#         collect = json.load(file)
#         print(json.dumps(collect, indent=4))
#         print(type(collect))
#     except json.JSONDecodeError:
#         print("❌ JSON ফাইলটি খালি বা invalid format-এ আছে।")
    
    
# print(dict(list_data))


print("Project 1 ..................................................")
import os
import json

file_path = "12) File_Handling\\file\\json.json"

# ✅ নতুন ডেটা
name = input("Type your Name: ")
age = int(input("Type Your Age: "))
location = input("Type your Location: ")
data = {
  "name":name,
  "age":age,
  "location":location
}

# ✅ Step 1: File exists কিনা দেখা 
if os.path.exists(file_path):
    try:
        # ✅ পুরাতন data read করে list আকারে রাখো
        with open(file_path, "r") as r:
            old_data = json.load(r)
            if not isinstance(old_data, list): #Check করে old_data লিষ্ট কি না, যদি লিষ্ট না হয়ে ডিস্ক হয় তবে সেটা লিষ্ট এ কনভার্ট করে 
                old_data = [old_data]
    except json.decoder.JSONDecodeError:
        old_data = []  # ফাইল খালি থাকলে

    # ✅ নতুন data যোগ করো
    old_data.append(data)

    # ✅ সব data লিখে দাও
    with open(file_path, "w") as w:
        json.dump(old_data, w, indent=4)
    print("✅ Your data has been saved successfully.")

else:
    print("❌ Please type valid file path.")
