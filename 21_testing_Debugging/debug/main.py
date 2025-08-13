# expense_tracker.py

def add_expense(expenses, category, amount):
    expenses.append({"category": category, "amount": amount})
    return expenses

def total_expense(expenses):
    total = sum(item["amount"] for item in expenses)
    return total

def expenses_by_category(expenses, category):
    filtered = [item for item in expenses if item["category"] == category]
    return filtered

# --- Main Program ---
if __name__ == "__main__":
    expenses = []

    # Breakpoint 1 - Start
    breakpoint()  # কোড শুরু হওয়ার আগে expenses খালি কিনা দেখো

    add_expense(expenses, "Food", "hyt")
    add_expense(expenses, "Transport", 50)
    add_expense(expenses, "Food", 80)

    # Breakpoint 2 - After Adding
    breakpoint()  # এখানে চেক করো expenses এর ভ্যালু ঠিক আছে কিনা

    print("Total Expense:", total_expense(expenses))

    # Breakpoint 3 - Filtered Data
    food_expenses = expenses_by_category(expenses, "Food")
    breakpoint()  # food_expenses এর মধ্যে সঠিক আইটেম আছে কিনা দেখো

    print("Food Expenses:", food_expenses)
