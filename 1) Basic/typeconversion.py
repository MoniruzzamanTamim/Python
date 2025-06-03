#Collect Data From User
# data = input("What's is your Name: \t")
# print(data)

import ast
import json

str_data1 = "HEllo This is Str"
str_data2 = "10"
str_data3 = "15.5"
int_data = 10
float_data = 1.58
bool_data = True
list_data = ["Tamim", 12,58, "five"]
tuple_data = ("hello-tuple", "tuple")
dict_data = {"name":"Tamim", "age":15, "vilage": "Dhaka" }
set_data = ("hello-set", "set")


#==> 1) int to  Other Data-Type 
print("Int  to Others Data Type.....................................")
c_i_s = str(int_data)
print("int to string",type( c_i_s))
c_i_flote = float(int_data)
print("int to Float",type( c_i_flote))
c_i_bool = bool(int_data)
print("int to Bool",type( c_i_bool))

#==> 2) Float to  Other Data-Type 
print("Float to Others Data Type.....................................")
c_f_s = str(float_data)
print("Float to string",type( c_f_s))
c_f_int = float(float_data)
print("Float to int",type( c_f_int))
c_f_bool = bool(float_data)
print("Float to Bool",type( c_i_bool))

#==> 2) Bool  to  Other Data-Type 
print("Bool to Others Data Type.....................................")
c_b_s = str(bool_data)
print("bool to string",type( c_b_s))
c_b_int = int(bool_data)
print("bool to int",type( c_b_int))
c_b_float = float(bool_data)
print("bool to Float",type( c_b_float))

print("..............................................")
#==> 1) String  to  Other Data-Type 
print("String to Others Data Type.....................................")
c_s_int = int(str_data2) # If String is  numeric ==> "10154"
print("String to int",type(c_s_int),c_s_int)

c_s_float = float(str_data3) # If String is  float ==> "101.25854" OR Number 
print("String to float",type(c_s_float),c_s_float)

c_s_bool = bool(str_data3) 
print("String to Bool",type(c_s_bool), c_s_bool)

#String to List 
print("..............................................")

c_s_list = list(str_data1) #Carekter String to list
print("String to List: ", c_s_list, type(c_s_list))

c_s_list2 = list(str_data2) #int string to list 
print("String to List: ", c_s_list2, type(c_s_list2))

c_s_list2 = list(str_data3)  #float string to list 
print("String to List: ", c_s_list2, type(c_s_list2))

#String to Tuple
print("..............................................")
c_s_t = tuple(str_data1)
print("String to Tuple: ",c_s_t, type(c_s_t))

c_s_t1 = tuple(str_data2)
print("String to Tuple: ",c_s_t1, type(c_s_t1))

c_s_t1 = tuple(str_data3)
print("String to Tuple: ",c_s_t1, type(c_s_t1))

#string to SET
print("..............................................")
c_s_set = set(str_data1)
print("String to SET: ",c_s_set, type(c_s_set))

c_s_set1 = set(str_data2)
print("String to SET: ",c_s_set1, type(c_s_set1))

c_s_set1 = set(str_data3)
print("String to SET: ",c_s_set1, type(c_s_set1))

#String to disk 
#Json Type Data String to Dict 
print(".................Json Type String Data Convert Dictionary.................")
s = '{"name": "Tamim", "age": 25}'  # এটি একটি JSON string
d = json.loads(s)
print(type(s))
print(d)
print(d["name"], type(d))  # Output: Tamim

#
print("...............Dict Type String Data Convert Dictionary .....................")
s = "{'name': 'Tamim', 'age': 25}"  # এটি JSON নয়, pure Python syntax
print(type(s))
d = ast.literal_eval(s)
print(d, type(d))


#==> 2) list   to  Other Data-Type 
print("List  to Others Data Type.....................................")

a = str(list_data)
print("list to String", a, type(a))
print(a)

a = bool(list_data)
print("list to Bool", a, type(a))


a = tuple(list_data)
print("list to Tuple", a, type(a))

a = set(list_data)
print("list to SET", a, type(a))


pairs = [["name", "Tamim"], ["age", 25]]
a = dict(pairs)
print("list to Dictionry ", a, type(a))