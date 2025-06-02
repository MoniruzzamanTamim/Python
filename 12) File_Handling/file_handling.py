
#Normal Read Data
f = open("Practise/demo.txt", "rt")
read_file = f.read()
f.close()
print(read_file)


#if Readable Return True 
f = open("Practise/demo.txt", "rt")
read_file = f.readable()
f.close()
print(read_file)

#1 line Read
f = open("Practise/demo.txt", "rt")
read_file = f.readline()
f.close()
print(read_file)


#read data on list mode
f = open("Practise/demo.txt", "rt")
read_file = f.readlines()
f.close()
print(read_file)



#Write Data overWring 

w = open("12) File_Handling/NewFile.txt", "wt")
w_data = w.write("Hello, Tamim, How Are You!")
print(w_data)
w.close()



a = open("12) File_Handling/NewFile.txt", "at")
a_data = a.write("\n This IS \"A\" , For Add Data With Ager Data thik rekhe ")
a.close()
print(a_data)