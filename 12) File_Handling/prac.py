import os 
import json
file_path = "12) File_Handling\\file\\prac.txt"

#Read File using I/) ==> read()
print("#Read File using I/) ==> readline() it Show All data from file")
r = open(file_path,"r")
r_data = r.read()
r.close()
print(r_data)

#Read File using I/) ==> read() on Check Path 
if os.path.exists(file_path):
    r = open(file_path, "r")
    view_data = r.read()
    view_data.close()
    print(view_data)
else:
    print("Please Entry Valid Path ")

#Read File using I/) ==> readline() it Show singel Line by Line
print("#Read File using I/) ==> readline() it Show singel Line by Line")
r = open(file_path,"r")
r_data = r.readline()
print(r_data)
print(r_data)

#Read File using I/) ==> readline() it Show all data as a list type
print("#Read File using I/) ==> readline() it Show all data as a list type")
r = open(file_path,"r")
r_data = r.readlines()
print(r_data)

#Write a some Value on File using I/) ==> write() method ==> w
w = open(file_path,"w")
w_data = w.write("Hello Tamim, you Added Some Data uning \"w\" method, this is a overwrite old data and start from start \n")
w.close()


#Write a some Value on File using I/) ==> write() method ==> a

a =  open(file_path,"a")
a_data = a.write("Add Some Data Using 'a' method, this method add data of last of file , no  data overwrite, old data is satable same to same")
a.close()


#Create a New File And Add Some Data, "x" method use only create and write data, old data is not suppoerted
# x = open("dict_data.py", "x")
# x_data = x.write("{'name': 'Tamim'}")
# x.close()
#
# x_read = open("dict_data.py", "r")
# x_data_view = x_read.read()
# print(x_data_view)



#Using + Plus method to Read & Write Data

rr = open(file_path,"r+")
rr_data = rr.read()
rr_write_data = rr.write("Hello Guys, this is r+ Method to add Data")
rr.close()
print(rr_data)


ww = open(file_path,"w+")
ww_data = ww.write("Hello Guys This w+ method, this method write file and read file but file old data overwrited")
ww_read_data = ww.read()
print(ww_read_data)

aa = open(file_path,"w+")
aa_data = ww.write("Hello Guys This a+ method, this method write file and read file ")
aa_read_data = ww.read()
print(aa_read_data)


#open File On use "with keyword"


with open(file_path, "r") as readfile:
    with_data = readfile.read()
print("with Statement:", with_data)


#Remove File 
if os.path.exists("deletedfile.txt"):
    os.remove("deletedfile.txt")
else:
    print("path file not suched")
