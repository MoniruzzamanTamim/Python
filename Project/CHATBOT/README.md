# 🤖 ChatBOT Application (Terminal-Based)
A terminal-based chatbot application written in Python that supports:
- 🔐 User authentication (Login, Signup, Delete Account)
- 💬 Chat interaction with predefined bot replies
- 📜 Chat history saved per user
- 🗑️ View & delete chat history

---
## 📁 Project Structure
Project/
└── CHATBOT/
├── ChatBOT.py                                      # 🔧 Main Python chatbot application
├── authenticitaionDB.json           # 🔐 User credentials database (JSON)
├── tamim_history.txt                       # 📝 Auto-created chat history per user
└── README.md                                       # 📄 Project documentation (this file)


## 🚀 How to Run
1. Open terminal and navigate to the `Project/CHATBOT/` folder.
2. Make sure `authenticitaionDB.json` exists (can be an empty `{}`).
3. Run the chatbot with:

python ChatBOT.py
🔐 Authentication
When you run the program, you’ll be prompted with:
1) LogIN
2) SignIN
3) Delete Account
✅ Stored in authenticitaionDB.json as:
json
{
  "tamim": {
    "userName": "tamim",
    "passWord": "tamim"
  }
}

🤖 Chat Commands
| User Input          | Bot Reply                                     |
| ------------------- | --------------------------------------------- |
| `hi` / `hello`      | Hello! How can I help you today?              |
| `how are you`       | I'm just a bot, but I'm doing great!          |
| `what is your name` | I'm PyBot – your Python-powered chatbot.      |
| `who created you`   | I was created by a Python developer like you! |
| `bye`               | Goodbye! Have a great day.                    |
| `exit`              | Exit the chat                                 |


📜 Chat History
After login, the main menu gives you options to:
1) Start Chat
2) Show Chat History
3) Delete History
4) Logout  Program
Chat logs are stored in username_history.txt, e.g., tamim_history.txt.

🛠 Built With
Python Standard Library only:
os
json
datetime
functools
time
No external packages required.


👤 Author
Tamim
Python Developer & Chatbot Creator
