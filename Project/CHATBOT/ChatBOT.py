from datetime import datetime
import os
from functools  import wraps
import time 
import json


current_user = None

def authentication(fun):
    @wraps(fun)
    def inner_decorator(*args, **kwargs):
        global current_user
        print("Welcome ChatBOT APPLication...")
        while True:
            try:
                print("\n1)LogIN \t2)SignIN")
                option = int(input("Choise an option: "))
            except Exception as e:
                print("Please Select Excact Option", e)
            
            authentication_path = r"Project\\CHATBOT\\authencitaionDB.json"
            if os.path.exists(authentication_path):
                with open(authentication_path, "r") as user_authen:
                    user_info= json.load(user_authen)
            else:
                print("Please Provide Correct File Path For Access User ")
            if option == 1:
                username = input("Type your UserName: ")
                password = input("Type your PassWord: ")
                for user_database, user_crediantial in user_info.items():
                    if username in user_database:
                        current_user = username
                        if username in user_crediantial["userName"] and password in user_crediantial["passWord"]:
                            fun(*args, **kwargs)
                            print(f"\nWelcome Chatbot  Application......{username.upper()}. ")
                            break
                        else:
                            print("Type Valid UserID! ," "If you don't have an account, please create one." )
                    else:
                        print("Your User ID Not Set Database, that's Why First SignUp the  Aplication")
            elif option ==2:
                print("SignUp Now.......")
                username = input("Type your UserName: ")
                password = input("Type your UserName: ")
                user_crediantial = {
                    "userName" : username,
                    "passWord": password
                }
                if username not in user_info:
                    user_info[username] = user_crediantial
                    if os.path.exists(authentication_path):
                        with open(authentication_path, "w") as sent_user_crediandial:
                            json.dump(user_info,sent_user_crediandial, indent=4)
                    print("Signup SuccessFully ... Now Login in Your Account")
                else:
                    print("This UserName Already Use Others Person, Please Create Unique Usename")
            elif option ==3:
                username = input("type UserName: ")
                if username in user_info:
                    del user_info[username]
                    if os.path.exists(authentication_path):
                        with open(authentication_path, "w") as sent_user_crediandial:
                            json.dump(user_info,sent_user_crediandial, indent=4)
                    print("Signup SuccessFully ... Now Login in Your Account")
                else:
                    print("This UserName Already Use Others Person, Please Create Unique Usename")
                
    return inner_decorator

class chatbot:
    def __init__(self,name,file):
        self.name = name
        self.file = file
        self.custom_message ={
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! 😊 ",
            "how are you": "I'm just a bot, but I'm doing great!",
            "what is your name": "I'm PyBot – your Python-powered chatbot.",
            "who created you": "I was created by a Python developer like you!",
            "bye": "Goodbye! Have a great day.",
        }
        
    def start(self, ):
        while True:
            try:
                current_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
                user_input = input("YOU: ").strip().lower()
                if  user_input == "exit":
                    print("BOT: Ok, Exit Chat,   See You Soon......")
                    break
                else:
                    # bot_reply = self.custom_message.get(user_input , "I don.t Know Your Command, Please Type Write Command") #Same kaj Korar jonno  nicher 8 line code, jar  madhume extra keyword dileo output dibe
                    found = False
                    for key in self.custom_message:
                        if key in user_input:
                            bot_reply = self.custom_message[key]
                            found = True
                            break
                        if not found:
                            bot_reply = "I don’t understand that. Please try a known command."
                    #Uporer 8 line code ak line diye kora jay  jeta uporer dike comment kora ache 
                    print(f"BOT: {bot_reply}")
                    log_chat = f"[{current_time}]  YOU: {user_input}\n[{current_time}]  BOT: {bot_reply}\n"
                    self.store_chat(log_chat)
                    
            except Exception as e:
                print(e)
    
    def store_chat(self,log_chat):
        
            try:
                with open(self.file, "a") as sent_data:
                    sent_data.write(log_chat)
            except Exception as e:
                print(f"Error writing chat:  Emoji Not Decode Text File {e}")
        
    def show_history(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as collect_data:
                print(collect_data.read())
        else:
            print("Kindly Provide Write File Location")
    
    def delete_history(self):
        if os.path.exists(self.file):
            open(self.file, "w").close()
            print("Your Chat History Clear  Successfully.....................")
        else:
            print("Kindly Provide Write File Location")

@authentication
def access():
    global current_user
    path = f"Project\\CHATBOT\\{current_user}_history.txt"
    chat = chatbot("Tamim", path)
    while True:
        print("\n==============================")
        print("🤖 ChatBOT APP")
        print("1) Start Chat")
        print("2) Show Chat History")
        print("3) Delete History")
        print("4) Exit Program")
        print("==============================")

        try:
            option = int(input("Choose an Option: "))
        except ValueError:
            print("❌ Please enter a valid number (1-4)")
            continue

        if option == 1:
            chat.start()
        elif option == 2:
            chat.show_history()
        elif option == 3:
            chat.delete_history()
        elif option == 4:
            print("👋 Exiting Program. Goodbye!")
            break
        else:
            print("❌ Invalid option! Please choose between 1 and 4.")



access()