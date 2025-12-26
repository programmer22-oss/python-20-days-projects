tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nTasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

    elif choice == '2':
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f'Task "{task}" added.')

    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            print("\nTasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f'Task "{removed_task}" removed.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Exiting the To-Do List application. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")