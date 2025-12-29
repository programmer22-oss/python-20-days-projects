expenses = []

def show_menu():
    print("\n💸 Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose option (1-4): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append({"name": name, "amount": amount})
        print("✅ Expense added")

    elif choice == "2":
        if not expenses:
            print("📭 No expenses recorded")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['name']} - ₹{expense['amount']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"💰 Total Expense: ₹{total}")

    elif choice == "4":
        print("👋 Exiting Expense Tracker")
        break

    else:
        print("⚠️ Invalid choice")
