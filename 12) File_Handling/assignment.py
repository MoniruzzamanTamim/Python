name = input("type your username: ")
age = int(input("Type your Age: "))

userinfo = f'name = {name}, age = {age}'
userData = open("userinformation.txt", "w")
sent_userData = userData.write(userinfo)
userData.close()


read_userData = open("userinformation.txt", "r")
data = read_userData.read()
print("Read Data: ", data)
read_userData.close()