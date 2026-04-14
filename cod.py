#To-Do list application in cod.py

tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def update_task():
    view_tasks()
    if tasks:
        num = int(input("\nEnter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[num - 1] = new_task
            print("Task updated!")
        else:
            print("Invalid number!")

def delete_task():
    view_tasks()
    if tasks:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed}' deleted!")
        else:
            print("Invalid number!")

# Main loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")