contacts = {}

def show_menu():
    print("\n📒 Contact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose option (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("✅ Contact added successfully")

    elif choice == "2":
        if not contacts:
            print("📭 No contacts available")
        else:
            print("\nContacts List:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(f"📞 {search} : {contacts[search]}")
        else:
            print("❌ Contact not found")

    elif choice == "4":
        delete = input("Enter name to delete: ")
        if delete in contacts:
            contacts.pop(delete)
            print("🗑️ Contact deleted")
        else:
            print("❌ Contact not found")

    elif choice == "5":
        print("👋 Exiting Contact Book")
        break

    else:
        print("⚠️ Invalid choice, try again")
