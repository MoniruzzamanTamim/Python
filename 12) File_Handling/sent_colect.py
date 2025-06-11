import os
import json
data = {
    "name": "Tamima",
    "age": 25,
    "location": {
        "country": "Bangladesh",
        "city": "Dhaka"
    },
    "languages": ["English", "Bengali"]
}



#View Data On Exiting File ==> Normal Way 


# import os
# if os.path.exists("C:\\Users\\X-Press\\Desktop\\Python\\Python\\12) File_Handling\\file\\json.json"):
#     with open("C:\\Users\\X-Press\\Desktop\\Python\\Python\\12) File_Handling\\file\\json.json", "r") as r:
#         read_data = r.read()
#         print(read_data)
#         print(type(read_data))
# else:
#     print("please Type valid File Path")



# #View Data On Exiting File ==>Convert Dict 


# if os.path.exists("C:\\Users\\X-Press\\Desktop\\Python\\Python\\12) File_Handling\\file\\json.json"):
#     with open("C:\\Users\\X-Press\\Desktop\\Python\\Python\\12) File_Handling\\file\\json.json", "r") as r:
#         read_data = json.load(r)
#         print(read_data)
#         print(type(read_data))
# else:
#     print("please Type valid File Path")


#Sent Dict Data-Type To Store Using File Handling


# import json
# if os.path.exists("C:\\Users\\X-Press\\Desktop\\Python\\Python\\12) File_Handling\\file\\json.json"):
#     with open("C:\\Users\\X-Press\\Desktop\\Python\\Python\\12) File_Handling\\file\\json.json", "a") as w:
#         json.dump(data,w, indent=4)
#         print("Your Data Sent Successfully")
# else:
#     print("please Type valid File Path")




import os
import json

# 🔹 Step 1: Data to be stored
list_data = [
    {"name": "Tamima", "age": 25},
    {"name": "Rahim", "age": 30}
]

# 🔹 Step 2: File path
file_path = r"C:\Users\X-Press\Desktop\Python\Python\12) File_Handling\file\json.json"

# 🔹 Step 3: Store data (overwrite or merge if file exists)
if os.path.exists(file_path):
    with open(file_path, "w") as w:
        json.dump(list_data, w)
        print("Data load Successfully")
else:
    print("Your Process Wrong")
    
print("\n📄 Showing JSON File Data:")


# 🔹 Step 6: Show Data
print("\n📄 Showing JSON File Data:")
with open(file_path, "r") as file:
    try:
        collect = json.load(file)
        print(json.dumps(collect, indent=4))
        print(type(collect))
    except json.JSONDecodeError:
        print("❌ JSON ফাইলটি খালি বা invalid format-এ আছে।")
    
    
print(dict(list_data))