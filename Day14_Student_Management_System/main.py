students = {}

def show_menu():
    print("\n🎓 Student Management Menu")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose option (1-5): ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("✅ Student added")

    elif choice == "2":
        if not students:
            print("📭 No student records")
        else:
            print("\nStudent List:")
            for roll, info in students.items():
                print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")

    elif choice == "3":
        roll = input("Enter roll number to update: ")
        if roll in students:
            marks = int(input("Enter new marks: "))
            students[roll]["marks"] = marks
            print("✏️ Marks updated")
        else:
            print("❌ Student not found")

    elif choice == "4":
        roll = input("Enter roll number to delete: ")
        if roll in students:
            students.pop(roll)
            print("🗑️ Student deleted")
        else:
            print("❌ Student not found")

    elif choice == "5":
        print("👋 Exiting system")
        break

    else:
        print("⚠️ Invalid choice")

print("Goodbye!")
