
# #Normal Read Data
# f = open("Practise/demo.txt", "rt")
# read_file = f.read()
# f.close()
# print(read_file)


# #if Readable Return True 
# f = open("Practise/demo.txt", "rt")
# read_file = f.readable()
# f.close()
# print(read_file)

# #1 line Read
# f = open("Practise/demo.txt", "rt")
# read_file = f.readline()
# f.close()
# print(read_file)


# #read data on list mode
# f = open("Practise/demo.txt", "rt")
# read_file = f.readlines()
# f.close()
# print(read_file)


# #Write Data overWring 
# w = open("12) File_Handling/NewFile.txt", "wt")
# w_data = w.write("Hello, Tamim, How Are You!")
# print(w_data)
# w.close()
# a = open("12) File_Handling/NewFile.txt", "at")
# a_data = a.write("\n This IS \"A\" , For Add Data With Ager Data thik rekhe ")
# a.close()
# print(a_data)

# # Open the file in append mode ("a") so it writes at the end of the file
# a = open("12) File_handling/file/file_handle.txt", "a")
# sent_data = a.write(" Hello This IS Write Data : ")
# a.close()



# # Open File as a With Keyword 
# with open("12) File_handling/file/file_handle.txt", "r") as a:
#     view_data = a.readline()
#     print(view_data)

# # Use Module to check path 
# import os

# if os.path.exists("12) File_handling/file/file_handle.txt"):
#      with open("12) File_handling/file/file_handle.txt", "r") as a:
#          view_data = a.readlines()
#          print(view_data)
# else:
#     print("Not Valid Path")


#Delete File 
import os

if os.path.exists("12) File_handling/files/file_handle.txt"):
     os.remove("12) File_handling/files/file_handle.txt")
else:
    print("Not Valid Path, Use Valid Path")