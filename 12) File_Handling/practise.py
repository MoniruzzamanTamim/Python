
import ast
import json


dict_value = {'disk': {
    "name":"Tamim",
    "age":25,
    "vilage":"Dhaka"
}}

f = open("12) File_Handling/dict.py", "wt")
data = f.write(str(dict_value))
f.close()






r = open("12) File_Handling/dict.py", "rt")
viewData = r.read()
r.close()
d = ast.literal_eval(viewData)
print(type(d))

print(d["disk"]["name"])
print(d["disk"]["age"])
print(d["disk"]["vilage"])






