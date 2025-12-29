import re

def notes_manager():
    note = input("Write your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("📝 Note saved")

def expense_tracker():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    with open("expenses.txt", "a") as file:
        file.write(f"{name},{amount}\n")
    print("💸 Expense added")

def password_checker():
    password = input("Enter password: ")
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    if strength <= 2:
        print("🔴 Weak Password")
    elif strength <= 4:
        print("🟡 Medium Password")
    else:
        print("🟢 Strong Password")

while True:
    print("\n🧰 Personal Utility App")
    print("1. Notes Manager")
    print("2. Expense Tracker")
    print("3. Password Strength Checker")
    print("4. Exit")

    choice = input("Choose option (1-4): ")

    if choice == "1":
        notes_manager()
    elif choice == "2":
        expense_tracker()
    elif choice == "3":
        password_checker()
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid choice")


