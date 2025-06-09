

#Expreanse Tracer 
import json
import ast

CATEGORIES = ["FOOD", "TOUR", "ENTERTRAINMENT", "OTHERS"]

expenses = []
def add():
    print("Please Add Your Expense Record: ")
    date = input("Enter date (YYYY-MM-DD): ")
    print("CATEGORIES: " , CATEGORIES)
    category = input("Please Type Your CATEGORI: ").upper()
    if category not in CATEGORIES:
        print("Categori not found!... \nPlease type valid categori....... " , CATEGORIES)
    ammount = int(input("Please Type Your Amoount: "))
    notes = input("Type Your Notes (OPTIONAL): ")

    expense = {
     "date": date,
     "category":category,
     "ammount": ammount,
     "notes": notes
    }
    expenses.append(expense)



def view():
    print("View Your Data....................")
    print("1. Monthly Based Record")
    print("2. Categori Based Record")
    choice = int(input("Type Your Choice: "))
    
    if (choice ==1):
        monthly = input("Type Month(MM): ")
        filtered = [e for e in expenses if e['date'][5:7] == monthly]
    elif choice == 2:
        Cat = input("Type Your Categori: ").upper()
        filtered = [e for e in expenses if e["category"]== Cat]
    else:
        print("Invalid choice")
        return


    if not filtered:
        print("No records found.")
        return

    for e in filtered:
        print(F"{e["date"]} | {e["category"]} | ${e['ammount']} | {e['notes']}")




def summery():
    print("Show in TOTAL, MAX, AVG SPENT")
    total = sum(e['ammount'] for e in expenses)
    avg = total/len(expenses)
    highest = max(expenses, key=lambda x: x["ammount"])
    
    
    print(f"Tolal Expense: ${total}" )
    print(f"Avg Expense: ${avg}" )
    print(f"Highest  Expense: ${highest} Cetegory:${highest['category']}, date{highest["date"]}, Amaount{highest['ammount']}" )



def store_in_file(filename="expenses.json"):
    with open(filename, "a") as f:
        json.dump(expenses, f) 
    f.close()                                                                       
    print("📁 Data saved to file.")1


def main():
    store_in_file()

    while True:
        print("\n📘 Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. List Tags")
        print("5. Save & Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            summery()
        elif choice == "4":
           store_in_file()
        elif choice == "5":
            store_in_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
