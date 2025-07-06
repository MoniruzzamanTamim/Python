file_path = "12) File_Handling\\file\\file_handle.txt"

# #Normal Read Data
# f = open(file_path, "rt")
# read_file = f.read()
# f.close()
# print(read_file)


# #if Readable Return True 
# f = open(file_path, "rt")
# read_file = f.readable()
# f.close()
# print(read_file)

# #1 line Read
# f = open(file_path", "rt")
# read_file = f.readline()
# f.close()
# print(read_file)


# #read data on list mode
# f = open(file_path, "rt")
# read_file = f.readlines()
# f.close()
# print(read_file)


# #Write Data overWring 
# w = open(file_path", "wt")
# w_data = w.write("Hello, Tamim, How Are You!")
# print(w_data)
# w.close()
# a = open(file_path, "at")
# a_data = a.write("\n This IS \"A\" , For Add Data With Ager Data thik rekhe ")
# a.close()
# print(a_data)

# # Open the file in append mode ("a") so it writes at the end of the file
# a = open(file_path, "a")
# sent_data = a.write(" Hello This IS Write Data : ")
# a.close()



# # Open File as a With Keyword 
# with open(file_path, "r") as a:
#     view_data = a.readline()
#     print(view_data)

# # Use Module to check path 
# import os

# if os.path.exists(file_path"):
#      with openfile_path, "r") as a:
#          view_data = a.readlines()
#          print(view_data)
# else:
#     print("Not Valid Path")


#Delete File 
import os
if os.path.exists(file_path):
     os.remove(file_path)
else:
    print("Not Valid Path, Use Valid Path")