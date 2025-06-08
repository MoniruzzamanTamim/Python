

#Expreanse Tracer 


CATEGORIES = ["FOOD", "TOUR", "ENTERTRAINMENT", "OTHERS"]

expenses = []
def add():
    print("Please Add Your Expense Record: ")
    date = input("Enter date (YYYY-MM-DD): ")
    print("CATEGORIES: " , CATEGORIES)
    category = input("Please Type Your CATEGORI: ").upper()
    if category not in CATEGORIES:
        print("Categori not found!... \nPlease type valid categori....... " , CATEGORIES)
    ammount = input("Please Type Your Amoount: ")
    notes = input("Type Your Notes (OPTIONAL): ")

    expense = {
     "date": date,
     "category":category,
     "ammount": ammount,
     "notes": notes
    }
    expenses.append(expense)

add()

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


view() 

def summery():
    print("Show in TOTAL, MAX, AVG SPENT")
    total = sum(e["ammount"] for e in expenses)
    avg = total/len(expenses)
    highest = max(expenses, key=lambda x: x["ammount"])
    
    
    print(f"Tolal Expense: ${total}" )
    print(f"Avg Expense: ${avg}" )
    print(f"Highest  Expense: ${highest} Cetegory:${highest['category']}, date{highest["date"]}, Amaount{highest['ammount']}" )


summery()